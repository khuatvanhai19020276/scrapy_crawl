import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { CrawlController } from './controllers/crawl.controller';
import { Crawl, CrawlSchema } from './schemas/crawl.schema';
import { CrawlService } from './services/crawl.service';

@Module({
  imports: [MongooseModule.forRoot('mongodb://localhost/database'),
            MongooseModule.forFeature([{name: Crawl.name, schema: CrawlSchema}])],
  controllers: [AppController, CrawlController],
  providers: [AppService, CrawlService],
})
export class AppModule {}
