import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ComponentsModule } from '@app/features/components/components.module';
import { HomeModule } from '@app/features/home/home.module';
import { SharedModule } from '@app/shared/shared.module';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CoreModule } from './core/core.module';
import { SmokerDetectorComponent } from './features/smoker-detector/smoker-detector.component';
import { PlayerComponent } from './features/smoker-detector/player/player.component';
import { SmokerServiceService } from '@app/features/smoker-detector/smoker-service.service';
import { MetadataEnhancementComponent } from './features/metadata-enhancement/metadata-enhancement.component';
import { MetadataServiceService } from '@app/features/metadata-enhancement/metadata-service.service';
import { UrlBoxComponent } from '@app/features/smoker-detector/url-box/url-box.component';
import { MetadataPlayerComponent } from './features/metadata-enhancement/metadata-player/metadata-player.component';
import { MetadataUrlBoxComponent } from './features/metadata-enhancement/metadata-url-box/metadata-url-box.component';
import { TagCloudComponent } from '@app/features/components/tag-cloud/tag-cloud.component';
import { SummaryComponent } from './features/metadata-enhancement/summary/summary.component';
import { ScoreBarComponent } from '@app/features/components/score-bar/score-bar.component';
import { ContextualAdvertisingComponent } from './features/contextual-advertising/contextual-advertising.component';
import { ContextualUrlBoxComponent } from './features/contextual-advertising/contextual-url-box/contextual-url-box.component';
import { ContextualServiceService } from '@app/features/contextual-advertising/contextual-service.service';
import { ContextualPlayerComponent } from './features/contextual-advertising/contextual-player/contextual-player.component';
import { AdBannerComponent } from '@app/features/components/ad-banner/ad-banner.component';
import { AdSummaryComponent } from './features/contextual-advertising/ad-summary/ad-summary.component';


@NgModule({
  imports: [
    // angular
    BrowserModule,
    BrowserAnimationsModule,

    // core & shared
    CoreModule,
    SharedModule,

    // features
    HomeModule,
    ComponentsModule,

    // app
    AppRoutingModule,
  ],
  providers: [SmokerServiceService, MetadataServiceService, ContextualServiceService],
  bootstrap: [AppComponent],
  declarations: [AppComponent, SmokerDetectorComponent, UrlBoxComponent, PlayerComponent, MetadataEnhancementComponent,
    MetadataPlayerComponent, MetadataUrlBoxComponent, TagCloudComponent, SummaryComponent, ScoreBarComponent,
    ContextualAdvertisingComponent, ContextualUrlBoxComponent, ContextualPlayerComponent, AdBannerComponent, AdSummaryComponent],
})
export class AppModule { }
