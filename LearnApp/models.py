from django.db import models

class Answer_manager(models.Manager):
    def st_patty(self, postData): 
        errors = {}

        if postData['question1'] != 3:
            errors['question1'] = "Question 1 is incorrect."
        if postData['question2'] != 1:
            errors['question2'] = "Question 2 is incorrect."
        if postData['question3'] != 2:
            errors['question3'] = "Question 3 is incorrect."
        if postData['question4'] != 3:
            errors['question4'] = "Question 4 is incorrect."

        return errors


class Student(models.Model):
    name = models.TextField(max_length=15)
    # user 
    # reading
    birthdate = models.DateTimeField()
    grade = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reading(models.Model):
    name = models.CharField(max_length=25)
    question1 = models.CharField(max_length=1)
    question2 = models.CharField(max_length=1)
    question3 = models.CharField(max_length=1)
    question4 = models.CharField(max_length=1)
    student = models.ManyToManyField(Student, related_name="reading")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Answer_manager()
    






    class Gov_QuizManager(models.Model):
    def gov_quiz_validate(self, postData):
        errors = {}

        if postData['queston1'] != 3:
            errors['question1']= 'Question 1 is incorrect'
        if postData['question2'] != 1:
            errors['question2'] = 'Questio 2 is incorrect'
        if postData['question3'] != 3:
            errors['question3'] = 'Question 3 is incorrect'
        if postData['quesion4'] != 2:
            errors['question4'] = 'Question 4 is incorrect'
        if postData['question5'] != 1:
            errors['question5'] = 'Question 5 is incorrect'
        return errors

class White_House_QuizManager(models.Model):
    def white_house_quiz_validate(self, postData):
        errors = {}

        if postData['queston1'] != 2:
            errors['question1']= 'Question 1 is incorrect'
        if postData['question2'] != 1:
            errors['question2'] = 'Questio 2 is incorrect'
        if postData['question3'] != 2:
            errors['question3'] = 'Question 3 is incorrect'
        if postData['quesion4'] != 3:
            errors['question4'] = 'Question 4 is incorrect'
        if postData['question5'] != 1:
            errors['question5'] = 'Question 5 is incorrect'
        return errors

class Declaratioon_QuizManager(models.Model):
    def declaration_quiz_validate(self, postData):
        errors = {}

        if postData['queston1'] != 1:
            errors['question1']= 'Question 1 is incorrect'
        if postData['question2'] != 3:
            errors['question2'] = 'Questio 2 is incorrect'
        if postData['question3'] != 1:
            errors['question3'] = 'Question 3 is incorrect'
        if postData['quesion4'] != 3:
            errors['question4'] = 'Question 4 is incorrect'
        if postData['question5'] != 2:
            errors['question5'] = 'Question 5 is incorrect'
        if postData['question6'] != 1:
            errors['question6'] = 'Question 6 is incorrect'
        return errors


class Gov_Quiz(models.Model):
    name = models.CharField(max_length=20)
    question1 = models.CharField(max_length=5)
    question2 = models.CharField(max_length=5)
    question3 = models.CharField(max_length=5)
    question4 = models.CharField(max_length=5)
    question5 = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Gov_QuizManager 

class White_House_Quiz(models.Model):
    name = models.CharField(max_length=20)
    question1 = models.CharField(max_length=5)
    question2 = models.CharField(max_length=5)
    question3 = models.CharField(max_length=5)
    question4 = models.CharField(max_length=5)
    question5 = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = White_House_QuizManager 

class Declaration_Quiz(models.Model):
    name = models.CharField(max_length=20)
    question1 = models.CharField(max_length=5)
    question2 = models.CharField(max_length=5)
    question3 = models.CharField(max_length=5)
    question4 = models.CharField(max_length=5)
    question5 = models.CharField(max_length=5)
    question6 = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Declaratioon_QuizManager