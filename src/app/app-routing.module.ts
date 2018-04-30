import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { homeRoutes } from './features/home/home.routes';
import { smokerDetectorRoutes} from '@app/features/smoker-detector/smoker-detector.routes';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  ...homeRoutes,
  ...smokerDetectorRoutes,
  {
    path: '**',
    redirectTo: 'home',
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule],
})
export class AppRoutingModule {}
