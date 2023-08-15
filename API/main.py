from fastapi import FastAPI, HTTPException
from model import Account, Application, Job

app = FastAPI()

data_store = []

job_seeker_account = Account("Utkarsh", "I am a Java Expert.", None, "Cloud Engineer", "Cisco", "JOB_SEEKER", None, None, None, None)


application1 = Application(None, None, "Cloud Engineer", "Microsoft")
application2 = Application(None, None, "Cloud Engineer", "Oracle")

job1 = Job("Cloud Engineer", "A Cloud Engineer deploys, debugs, and executes initiatives related to cloud computing. They design, develop, and maintain cloud-based systems, ensuring efficient data storage and adherence to security policies. They also interact with clients, provide cloud support, and make recommendations based on client needs.", "https://jobs.cisco.com/", "25 LPA", "Bengaluru", None, "FULL_TIME", "NO", [application1])

job2 = Job("Backend Engineer", "A Cloud Engineer deploys, debugs, and executes initiatives related to cloud computing. They design, develop, and maintain cloud-based systems, ensuring efficient data storage and adherence to security policies. They also interact with clients, provide cloud support, and make recommendations based on client needs.", "https://jobs.cisco.com/", "25 LPA", "Bengaluru", None, "FULL_TIME", "NO", [application2])

all_jobs = [job1, job2]

employer_account = Account("Cisco", "Cisco Systems, Inc., commonly known as Cisco, is an American-based multinational digital communications technology conglomerate corporation headquartered in San Jose, California.", None, None, None, "EMPLOYER", "Chuck Robbins", "86000", "1984", all_jobs)

# GET All Job 
@app.get("/job")
def getAllJob():
    return all_jobs

# GET All Job by Id 
@app.get("/job/{employer_name}")
def getJobByEmployer(employer_name: str):
    return employer_account.job_listing

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
