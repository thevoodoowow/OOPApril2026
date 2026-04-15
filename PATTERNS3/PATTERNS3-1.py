class Resume:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.phone = ""
        self.summary = ""
        self.experience = []
        self.education = []
        self.skills = []
        self.languages = []
        self.certifications = []

    def __str__(self) -> str:
        return (
            f"=== {self.name} ===\n"
            f"Email: {self.email} | Тел: {self.phone}\n"
            f"Навыки: {', '.join(self.skills)}\n"
            f"Опыт: {len(self.experience)} поз. | Образование: {len(self.education)} поз.\n"
        )


class ResumeBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._resume = Resume()
        return self

    def set_name(self, name: str):
        self._resume.name = name
        return self

    def set_contacts(self, email: str, phone: str = "88005553535"):
        self._resume.email = email
        self._resume.phone = phone
        return self

    def add_experience(self, company: str, years: int):
        self._resume.experience.append({"company": company, "years": years})
        return self

    def add_education(self, degree: str, school: str):
        self._resume.education.append({"degree": degree, "school": school})
        return self

    def add_skill(self, skill: str):
        self._resume.skills.append(skill)
        return self

    def build(self) -> Resume:
        product = self._resume
        self.reset()
        return product


class Director:
    def __init__(self, builder: ResumeBuilder):
        self.builder = builder

    def build_minimal_resume(self, name: str, email: str):
        return self.builder.set_name(name).set_contacts(email).build()

    def build_pro_resume(self, name: str, email: str):
        return (
            self.builder.set_name(name)
            .set_contacts(email)
            .add_experience("Global Tech", 5)
            .add_education("PhD", "MIT")
            .add_skill("Python")
            .add_skill("System Design")
            .add_skill("Kubernetes")
            .build()
        )


builder = ResumeBuilder()
director = Director(builder)

pro_resume = director.build_pro_resume("Иван Петров", "ivan@tech.com")
print("Стандартное резюме:")
print(pro_resume)

custom_resume = (
    builder.set_name("Анна Иванова")
    .set_contacts("anna@example.com", "+7-9003001488")
    .add_skill("React")
    .build()
)
print("Расширенное резюме:")
print(custom_resume)
