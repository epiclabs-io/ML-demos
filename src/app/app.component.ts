import { routerTransition } from '@app/core';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  animations: [routerTransition],
})
export class AppComponent {
  logoPath = '/assets/imgs/epic_labs_logo_145x55.png';

  sections = [
    {
      route: '/home',
      title: 'Home',
    }, {
      route: '/smokerDetector',
      title: 'Smoker Detector'
    }
  ];
}

