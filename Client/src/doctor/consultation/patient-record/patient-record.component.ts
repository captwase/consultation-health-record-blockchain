import { Component, Input, OnInit, Output, EventEmitter } from "@angular/core";
import { DoctorService } from "src/doctor/services/doctor.service";
import { Symptoms } from "src/utils/Symptoms";

type MedicationType = [
  {
    name: "";
    dose: "";
    frequency: "";
    nofDays: "";
    remarks: "";
  }
];

type PatientMedicalrecordType = {
  Diagnosis: "";
  Medication: MedicationType;
  ClinicalTest: [];
};

@Component({
  selector: "app-patient-record",
  templateUrl: "./patient-record.component.html",
  styleUrls: ["./patient-record.component.sass"],
})
export class PatientRecordComponent implements OnInit {
  @Input() PatientDetails: any = {};
  @Input() PatientRecords: any = {};
  @Output() saveRecord = new EventEmitter<any>();

  model: any;

  Medication: any[] = [];
  ClinicalTest: any[] = [];

  med: any = {};
  clinic: any = {};

  LabFiles: any[] = [];


  constructor(private ds: DoctorService) {
    this.model = {};
  }

  ngOnInit(): void {
    console.log();
    this.model = this.PatientRecords.data || {};
    console.log(this.model);

    this.Medication = this.model.medication || [];
    this.ClinicalTest = this.model.tests || [];
    this.LabFiles = this.model.files || [];

  }

  onMedicinesSave() {
    this.Medication.push(this.med);
    this.med = {};
  }

  onTestSave() {
    this.ClinicalTest.push(this.clinic);
    this.clinic = {};
  }

  onPatientRecordSubmit() {
    this.model.medication = this.Medication;
    this.model.tests = this.ClinicalTest;
    this.model.files = this.LabFiles;

    console.log(this.model);
    this.saveRecord.emit(this.model);
    this.model = {};
    this.Medication = [];
    this.ClinicalTest = [];
  }


  onFileAdd(files: any) {
    for (let i = 0; i < files.target.files.length; i++) {
      var reader = new FileReader();
      reader.onload = (event: any) => {
        this.LabFiles[i] = event.target.result;
      };
      reader.readAsDataURL(files.target.files[i]);
    }
  }
}
