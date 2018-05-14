import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { homeRoutes } from './features/home/home.routes';
import { smokerDetectorRoutes } from '@app/features/smoker-detector/smoker-detector.routes';
import { metadataEnhancementRoutes } from '@app/features/metadata-enhancement/metadata-enhancement.routes';
import { contextualAdvertisingRoutes } from '@app/features/contextual-advertising/contextual-advertising.routes';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  ...homeRoutes,
  ...smokerDetectorRoutes,
  ...metadataEnhancementRoutes,
  ...contextualAdvertisingRoutes,
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
