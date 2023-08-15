class Account:
    def __init__(self, name, bio, photo, current_job_title, current_company, profile_type, ceo, company_size, year_founded, job_listing):
        self.name = name
        self.bio = bio
        self.photo = photo
        self.current_job_title = current_job_title
        self.current_company = current_company
        self.profile_type = profile_type
        self.ceo = ceo
        self.company_size = company_size
        self.year_founded = year_founded
        self.job_listing = job_listing


class Job:
    def __init__(self, role_title, description, website_link, salary, location, company_user, job_type, completed, application):
        self.role_title = role_title
        self.description = description
        self.website_link = website_link
        self.salary = salary
        self.location = location
        self.company_user = company_user
        self.job_type = job_type
        self.completed = completed
        self.application = application


class Application:
    def __init__(self, resume, cover_letter, current_role, current_company):
        self.resume = resume
        self.cover_letter = cover_letter
        self.current_role = current_role
        self.current_company = current_company
