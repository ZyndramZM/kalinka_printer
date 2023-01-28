from django.db import models
from django.contrib.auth import get_user_model
from kalinka_printer.settings import BASE_DIR

UPLOAD_DIR = BASE_DIR / 'printer' / 'uploads'


# UPLOAD_DIR_PDF = BASE_DIR / 'printer' / 'uploads' / 'pdf'


class Document(models.Model):
    class Orientation(models.TextChoices):
        P = 'P', "Pionowa"
        L = 'L', "Pozioma"

    class NotReadyToPrint(Exception):
        pass

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file = models.FileField(upload_to=UPLOAD_DIR)
    # file_pdf = models.FileField(upload_to=UPLOAD_DIR_PDF, null=True, blank=True)
    mono = models.BooleanField(default=False)
    pages = models.IntegerField(null=True, blank=True)
    orientation = models.CharField(
        max_length=1,
        choices=Orientation.choices,
        default=Orientation.P,
    )
    ready_to_print = models.BooleanField(default=False)
    editable = models.BooleanField(default=True)

    def __str__(self):
        return f"Document {self.file.name}; owner: {self.user}"

    def discover(self):
        from PyPDF2 import PdfReader
        f = self.file.open('rb')
        try:
            pdf = PdfReader(f)
            self.pages = pdf.getNumPages()
        except:
            raise Document.NotReadyToPrint("Unable to read document.")

        f.close()
        self.ready_to_print = True


    def print(self):
        if not self.ready_to_print:
            raise Document.NotReadyToPrint("Nie wszystkie opcje zostały wybrane.")

        self.editable = False


class PrintJob(models.Model):
    class Status(models.TextChoices):
        ST = 'ST', "Nadany"
        PD = 'PD', "Oczekuje"
        IN = 'IN', "W trakcie drukowania"
        OK = 'OK', "Ukończono"
        FD = 'FD', "Błąd"

    set_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.ST
    )
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
