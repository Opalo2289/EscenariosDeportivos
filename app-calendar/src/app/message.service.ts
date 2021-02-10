import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class MessageService {


  constructor(
    private snackBar: MatSnackBar,
  ) { }

  //Esto no se puede tocar
  openSnackBar(message: string, action: string, duration: number = 12000) {
    this.snackBar.open(message.toUpperCase(), action, {
      duration,
      horizontalPosition: 'center',
      verticalPosition: 'top'
    });
  }
}