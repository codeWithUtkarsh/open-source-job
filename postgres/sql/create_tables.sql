CREATE TABLE account (
    id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	bio VARCHAR ( 255 ),
	photo bytea,
	current_job_title VARCHAR ( 50 ),
	current_company VARCHAR ( 50 ),
    profile_type  VARCHAR ( 50 ),
    ceo  VARCHAR ( 50 ),
    company_size  VARCHAR ( 50 ),
    year_founded  VARCHAR ( 50 ),
    job_listing  text ARRAY
);