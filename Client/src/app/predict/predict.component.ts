import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Symptoms } from 'src/utils/Symptoms';

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.sass']
})
export class PredictComponent implements OnInit {


  DiseaseSymptoms = Symptoms

  SelectedSymptoms!: string[];
  symptom: string = ''

  predictedDisease: string = ''
  predicting: boolean = false
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.SelectedSymptoms = new Array<string>()
  }

  addSymptom() {
    if (!this.SelectedSymptoms.includes(this.symptom) && this.SelectedSymptoms.length <= 17)
      this.SelectedSymptoms.push(this.symptom)
    this.symptom = ''
  }

  removeSymptom(i: number) {
    console.log(this.SelectedSymptoms[i]);
    this.SelectedSymptoms = this.SelectedSymptoms.filter(symptom => { return this.SelectedSymptoms[i] !== symptom })
  }

  predict() {
    this.predicting = true
    this.predictDisease(this.SelectedSymptoms).subscribe((r: any) => {
      this.predictedDisease = r.disease
      this.predicting = false
    })
  }

  predictDisease(symptoms: string[]) {
    return this.http.post("http://localhost:8000/api/predict_disease/", { symptoms: symptoms })
  }
}
