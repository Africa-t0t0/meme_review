set -e
export PGPASSWORD=$POSTGRES_PASSWORD;

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL

CREATE USER $POSTGRES_USER WITH PASSWORD $POSTGRES_PASSWORD;
CREATE DATABASE $POSTGRES_DB;
GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;

\connect $POSTGRES_DB $POSTGRES_USER
BEGIN;
CREATE TABLE memes (
        meme_id integer NOT NULL,
        meme_name varchar,
        meme_ranking integer,
        meme_story text,
        meme_image text
    );
COMMIT;
EOSQL
