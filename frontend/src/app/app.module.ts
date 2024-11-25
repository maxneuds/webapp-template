import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common'; // Import here
import { AppComponent } from './app.component'; // Your component
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';


@NgModule({
  declarations: [],
  imports: [BrowserModule, AppComponent, CommonModule, FormsModule, BrowserAnimationsModule],  // Add to NgModule imports
  bootstrap: []
})
export class AppModule { }
