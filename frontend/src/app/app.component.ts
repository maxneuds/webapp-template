import { Component, OnInit } from '@angular/core';
import { animate, state, style, transition, trigger } from '@angular/animations';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  standalone: true,
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [CommonModule, FormsModule],
  animations: [
    trigger('bannerState', [
      state('hidden', style({ transform: 'translateY(100%)' })),
      state('shown', style({ transform: 'translateY(0)' })),
      transition('hidden => shown', animate('300ms ease-in')),
      transition('shown => hidden', animate('300ms ease-out')),
    ]),
  ],
})
export class AppComponent implements OnInit {
  inputText: string = '';
  showBanner: boolean = false;
  countdown: number = 0;

  ngOnInit() {
    const bannerStyle = document.createElement('style');
    bannerStyle.innerHTML = `
      .banner {
        position: fixed;
        top: 0; /* Top of the page */
        left: 0;
        width: 100%; /* Full width */
        height: 20px;
        background-color: #4CAF50;
        color: white;
        padding: 20px;
        border-radius: 0; /* No rounded corners */
        font-size: 2em;
        z-index: 1000;
        opacity: 0.8; /* Add opacity */
        display: flex; /* Use flexbox for alignment */
        justify-content: center; /* Center text horizontally */
        align-items: center; /* Center text vertically */
      }
    `;
    setTimeout(() => {
      const bannerElement = document.querySelector('.banner'); // Get banner element
      if (bannerElement) {
        bannerElement.remove();  // Remove the banner from the DOM
      }
    }, 3000); // Remove after 3 seconds
    document.head.appendChild(bannerStyle);
  }

  showPopup() {
    if (this.inputText.trim() !== '') {
      this.showBanner = true;
      this.countdown = 3; // Start countdown

      const interval = setInterval(() => {
        this.countdown--;
        if (this.countdown === 0) {
          clearInterval(interval);
          this.showBanner = false;
        }
      }, 1000);
    }
  }

  onEnter(event: KeyboardEvent) {  // New method for Enter key press
    if (event.key === 'Enter') {
      this.showPopup();
    }
  }
}