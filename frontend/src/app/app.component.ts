import { Component } from '@angular/core';
import { NewsService } from './news.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  selectedCategory: string = '';
  item: string = '';
  newsData: any;

  constructor(private newsService: NewsService) {}

  onChange() {
    console.log(this.item);

    this.newsService.getNews(this.item || this.selectedCategory)
      .subscribe(response => {
        // Assign the API response data to the newsData variable
        this.newsData = response;
        console.log(this.newsData)
      });
  }
}
