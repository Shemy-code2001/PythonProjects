from datetime import date, time, datetime, timedelta

class Patient:
    auto = 1
    def __init__(self, n, p, d=None):
        self.__code = Patient.auto
        Patient.auto += 1
        self.__name = n
        self.__surname = p
        self.__birthdate = d
    
    @property
    def code(self):
        return self.__code
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, nv):
        self.__name = nv
    
    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, nv):
        self.__surname = nv
    
    @property
    def birthdate(self):
        return self.__birthdate
    
    @birthdate.setter
    def birthdate(self, nv):
        self.__birthdate = nv
    
    def __str__(self):
        return f"""code: {self.code}, name: {self.name}, surname: {self.surname}
birthdate: {self.birthdate}"""
    
    def __eq__(self, other):
        return self.__code == other.__code
    
    def __gt__(self, other):
        return self.birthdate > other.birthdate
    
    def __ge__(self, other):
        return self.birthdate >= other.birthdate

from abc import ABC, abstractmethod

class Consultation(ABC):
    def __init__(self, dateC=None, H=time(0, 0), p=None, m=0):
        self.__consultation_date = dateC
        self.__hour = H
        self.__patient = p
        self.__amount = m
    
    @property
    def consultation_date(self):
        return self.__consultation_date
    
    @consultation_date.setter
    def consultation_date(self, nv):
        self.__consultation_date = nv
    
    @property
    def hour(self):
        return self.__hour
    
    @hour.setter
    def hour(self, nv):
        self.__hour = nv
    
    @property
    def patient(self):
        return self.__patient
    
    @patient.setter
    def patient(self, nv):
        self.__patient = nv
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, nv):
        self.__amount = nv
    
    @abstractmethod
    def calculate_doctor_fee(self):
        pass

class DiagnosticConsultation(Consultation):
    def __init__(self, t="", echo=False, d=None, H=None, p="", m=0):
        self.__type = t
        self.__ultrasound = echo
        super().__init__(d, H, p, m)
    
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, nv):
        self.__type = nv
    
    @property
    def ultrasound(self):
        return self.__ultrasound
    
    @ultrasound.setter
    def ultrasound(self, nv):
        self.__ultrasound = nv
    
    def calculate_doctor_fee(self):
        if not self.__ultrasound:
            return self.amount + 50
        else:
            return self.amount + 100

class CheckupConsultation(Consultation):
    def __init__(self, t, d=None, H=None, p="", m=0):
        self.__type = t
        super().__init__(d, H, p, m)
    
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, nv):
        if nv.lower() not in ['analysis', 'consultation']:
            print("The checkup type must be 'Analysis' or 'Consultation'.")
        self.__type = nv
    
    def calculate_doctor_fee(self):
        if self.__type.lower() == 'analysis':
            return 0
        elif self.__type.lower() == 'consultation':
            return self.amount - 50

class Appointment:
    def __init__(self, d=datetime(1, 1, 1), p=None, obs=""):
        if d < datetime.today():
            print("The date must be later than today's date.")
        else:
            self.__date = d
        self.__patient = p
        self.__observation = obs
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, nv):
        if nv < datetime.today():
            print("The date must be later than today's date.")
        self.__date = nv
    
    @property
    def patient(self):
        return self.__patient
    
    @patient.setter
    def patient(self, nv):
        self.__patient = nv
    
    @property
    def observation(self):
        return self.__observation
    
    @observation.setter
    def observation(self, nv):
        self.__observation = nv

class MedicalOffice:
    def __init__(self, lP=[], lC=[], lrdz=[]):
        self.Lpatients = lP
        self.Lcns = lC
        self.Lrdz = lrdz
    
    def add_patient(self, patient):
        if isinstance(patient, Patient):
            self.Lpatients.append(patient)
            print("Patient added successfully.")
        else:
            print("A Patient object must be added to the list.")
    
    def existing_patient(self, n, p):
        for i in self.Lpatients:
            if i.name == n and i.surname == p:
                return i.code
        return -1
    
    def add_appointment(self, appointment):
        if isinstance(appointment, Appointment):
            if appointment not in self.Lrdz:
                self.Lrdz.append(appointment)
                print("Appointment added successfully.")
            else:
                print("Date already occupied.")
        else:
            print("Error.")
    
    def show_appointments_for_today(self, date):
        appointments_today = []
        for i in self.Lrdz:
            if i.date.date() == date:
                appointments_today.append(i)
        return appointments_today
    
    def patients_with_visits(self):
        one_week_ago = datetime.today() - timedelta(7)
        patients = []
        for i in self.Lcns:
            if i.date <= datetime.today() and i.date > one_week_ago:
                patients.append(i.patient)
        return patients
    
    def remove_patient(self, patient):
        for i in self.Lpatients:
            if i == patient:
                self.Lpatients.remove(i)
                break
        self.Lcns = [i for i in self.Lcns if i.patient != patient]
        self.Lrdz = [i for i in self.Lrdz if i.patient != patient]
        return "Patient removed successfully."
    
    def cancel_appointment(self, appointment):
        if isinstance(appointment, Appointment):
            if appointment in self.Lrdz:
                self.Lrdz.remove(appointment)
                return "Appointment canceled."
            else:
                return "Appointment not found."
        return "Error."

# Main program:
# timedelta object expressing the difference (in days) between 2 date or datetime objects
d1 = date(2000, 4, 6)
d2 = date(1996, 3, 7)
td = d1 - d2  # result will be a timedelta object

# Creating a timedelta object
# timedelta constructor (days, seconds, microseconds, milliseconds, minutes, hours, weeks)
# str of the timedelta object returns the string: {days} days, {hours}:{minutes}:{seconds}:{microseconds}:{milliseconds}
td1 = timedelta(days=12, hours=34, minutes=67, seconds=86, milliseconds=12, microseconds=23, weeks=1)
td2 = timedelta(seconds=5)
