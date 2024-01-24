class CollegePlacementSystem:
    def __init__(self):
        self.students = {}
        self.jobs = {}

    def add_student(self, student_id, name, skills):
        self.students[student_id] = {'name': name, 'skills': skills, 'placement': None}

    def add_job(self, job_id, title, required_skills):
        self.jobs[job_id] = {'title': title, 'required_skills': required_skills, 'filled': False}

    def display_students(self):
        print("\nStudents:")
        for student_id, details in self.students.items():
            print(f"{student_id}: {details['name']} - Skills: {details['skills']} - Placement: {details['placement']}")

    def display_jobs(self):
        print("\nJobs:")
        for job_id, details in self.jobs.items():
            status = "Filled" if details['filled'] else "Available"
            print(f"{job_id}: {details['title']} - Required Skills: {details['required_skills']} - Status: {status}")

    def match_students_to_jobs(self):
        for job_id, job_details in self.jobs.items():
            if not job_details['filled']:
                for student_id, student_details in self.students.items():
                    if not student_details['placement'] and set(job_details['required_skills']).issubset(set(student_details['skills'])):
                        # Match found
                        student_details['placement'] = job_details['title']
                        job_details['filled'] = True
                        break

    def run_placement_system(self):
        # Sample data
        self.add_student(1, 'Pritam', ['Python', 'Java', 'C++'])
        self.add_student(2, 'Koyana', ['Java', 'JavaScript'])
        self.add_student(3, 'Chinmoy', ['Python', 'C#'])

        self.add_job(101, 'Software Developer', ['Python', 'Java'])
        self.add_job(102, 'Web Developer', ['JavaScript', 'HTML', 'CSS'])
        self.add_job(103, 'Data Analyst', ['Python', 'SQL'])

        # Display initial state
        self.display_students()
        self.display_jobs()

        # Match students to jobs
        self.match_students_to_jobs()

        # Display final state
        print("\nPlacement Results:")
        self.display_students()
        self.display_jobs()

if __name__ == "__main__":
    placement_system = CollegePlacementSystem()
    placement_system.run_placement_system()
