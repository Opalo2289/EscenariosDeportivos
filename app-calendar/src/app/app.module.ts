import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ServiceWorkerModule } from '@angular/service-worker';
import { environment } from '../environments/environment';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import {NgbPaginationModule, NgbAlertModule} from '@ng-bootstrap/ng-bootstrap';
import { FullCalendarModule } from '@fullcalendar/angular'; // the main connector. must go first
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/daygrid';
import listPlugin from '@fullcalendar/interaction';
import interactionPlugin from '@fullcalendar/interaction';
import { CalendarComponent } from './calendar/calendar.component'; // a plugin
import { HttpClientModule } from "@angular/common/http";
import { SelectDropDownModule } from 'ngx-select-dropdown'

FullCalendarModule.registerPlugins([ // register FullCalendar plugins
  dayGridPlugin, 
  timeGridPlugin,
  listPlugin,
  interactionPlugin
]);


@NgModule({
  declarations: [
    AppComponent,
    CalendarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ServiceWorkerModule.register('ngsw-worker.js', { enabled: environment.production }),
    NgbModule,
    NgbPaginationModule,
    NgbAlertModule,
    FullCalendarModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    SelectDropDownModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
