import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  private apiUrl = 'http://localhost:8000/api/news/';

  constructor(private http: HttpClient) { }

  getNews(item: string, category?: string) {
    // Append the value to the API URL
    let url: string
     if (category) {
       url = `${this.apiUrl}?category=${category}`;
    } else {
       url = `${this.apiUrl}?item=${item}`;
    }

    return this.http.get(url);
  }
}
