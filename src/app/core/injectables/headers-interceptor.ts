import {Injectable} from '@angular/core';
import {HttpEvent, HttpInterceptor, HttpHandler, HttpRequest, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';

@Injectable()
export class HeadersInterceptor implements HttpInterceptor {
  constructor() {}

  intercept(req: HttpRequest<any>, next: HttpHandler):
  Observable<HttpEvent<any>> {
    // Clone the request to add the new header.
    const headeredReq = req.clone({headers: req.headers.set('Content-Type', 'application/json')});
    // Pass on the cloned request instead of the original request.
    return next.handle(headeredReq);
  }
}
