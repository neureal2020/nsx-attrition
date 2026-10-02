-- Neurosurgery residency attrition database
-- Design principle: OBSERVATIONS (what a source literally said, with a date)
-- are stored separately from INFERENCES (attrition status). Every inference
-- must be traceable to observations. Never overwrite an observation.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS programs (
    program_id      INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    city            TEXT,
    state           TEXT,          -- US state / CA province / MX state
    country         TEXT NOT NULL DEFAULT 'US',
    acgme_id        TEXT,          -- 10-digit ACGME program ID, filled later
    nrmp_code       TEXT,
    website         TEXT,          -- from AANS directory
    roster_url      TEXT,          -- specific page listing current residents
    roster_url_verified_on TEXT,
    positions_per_year INTEGER,    -- approved complement, for denominator
    active          INTEGER DEFAULT 1,
    source          TEXT,
    notes           TEXT
);

-- One row per time we captured a roster page (live fetch or Wayback snapshot)
CREATE TABLE IF NOT EXISTS roster_snapshots (
    snapshot_id     INTEGER PRIMARY KEY,
    program_id      INTEGER NOT NULL REFERENCES programs(program_id),
    source_url      TEXT NOT NULL,
    source_type     TEXT NOT NULL CHECK (source_type IN ('live','wayback','manual','instagram','other')),
    captured_at     TEXT NOT NULL,     -- ISO date the SOURCE reflects
    retrieved_at    TEXT NOT NULL,     -- ISO date WE pulled it
    academic_year   TEXT,              -- inferred, e.g. '2024-2025'
    html_path       TEXT,              -- local archived copy
    parse_status    TEXT DEFAULT 'unparsed',
    notes           TEXT,
    UNIQUE(program_id, source_url, captured_at)
);

-- The person. One row per human being, deduplicated across programs/years.
CREATE TABLE IF NOT EXISTS residents (
    resident_id     INTEGER PRIMARY KEY,
    full_name       TEXT NOT NULL,
    first_name      TEXT,
    middle_name     TEXT,
    last_name       TEXT,
    suffix          TEXT,
    degrees         TEXT,              -- MD, DO, MD/PhD
    med_school      TEXT,
    med_school_grad_year INTEGER,
    match_year      INTEGER,           -- year they entered PGY-1
    match_program_id INTEGER REFERENCES programs(program_id),
    name_variants   TEXT,              -- JSON array of alternate spellings seen
    notes           TEXT
);

-- Core evidence table: "source X, dated Y, listed person Z at program P as PGY-N"
CREATE TABLE IF NOT EXISTS roster_observations (
    obs_id          INTEGER PRIMARY KEY,
    snapshot_id     INTEGER NOT NULL REFERENCES roster_snapshots(snapshot_id),
    program_id      INTEGER NOT NULL REFERENCES programs(program_id),
    resident_id     INTEGER REFERENCES residents(resident_id),  -- NULL until matched
    name_as_listed  TEXT NOT NULL,
    pgy_as_listed   TEXT,
    pgy_numeric     INTEGER,
    academic_year   TEXT,
    role            TEXT,              -- resident / fellow / chief / research
    raw_context     TEXT
);

-- Inferred status. Derived from observations + external verification.
CREATE TABLE IF NOT EXISTS outcomes (
    outcome_id      INTEGER PRIMARY KEY,
    resident_id     INTEGER NOT NULL REFERENCES residents(resident_id),
    status          TEXT NOT NULL CHECK (status IN (
                        'in_training','graduated','transferred_out','transferred_in',
                        'switched_specialty','left_medicine','deceased',
                        'attrition_unspecified','unknown')),
    last_seen_ay    TEXT,              -- last academic year observed in program
    last_seen_pgy   INTEGER,
    departure_ay    TEXT,              -- academic year they vanished
    destination_program_id INTEGER REFERENCES programs(program_id),
    destination_specialty  TEXT,
    confidence      TEXT CHECK (confidence IN ('confirmed','probable','possible','unverified')),
    evidence        TEXT,              -- free text: what proves this
    adjudicated_by  TEXT,
    adjudicated_on  TEXT,
    UNIQUE(resident_id)
);

-- External identifiers used to adjudicate outcomes
CREATE TABLE IF NOT EXISTS external_ids (
    ext_id          INTEGER PRIMARY KEY,
    resident_id     INTEGER NOT NULL REFERENCES residents(resident_id),
    source          TEXT NOT NULL CHECK (source IN ('npi','abns','state_license','doximity','linkedin','pubmed','program_site','other')),
    value           TEXT,
    url             TEXT,
    payload         TEXT,              -- JSON blob of what we retrieved
    retrieved_on    TEXT,
    match_confidence TEXT
);

CREATE INDEX IF NOT EXISTS idx_obs_program ON roster_observations(program_id);
CREATE INDEX IF NOT EXISTS idx_obs_resident ON roster_observations(resident_id);
CREATE INDEX IF NOT EXISTS idx_obs_name ON roster_observations(name_as_listed);
CREATE INDEX IF NOT EXISTS idx_snap_program ON roster_snapshots(program_id);
CREATE INDEX IF NOT EXISTS idx_res_last ON residents(last_name);
