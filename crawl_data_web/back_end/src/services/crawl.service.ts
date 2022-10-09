import { Injectable } from "@nestjs/common";
import { InjectModel } from "@nestjs/mongoose";
import { Model } from "mongoose";
import { Crawl, CrawlDocument } from "src/schemas/crawl.schema";

@Injectable()
export class CrawlService {

    constructor(@InjectModel(Crawl.name) private crawlModel: Model<CrawlDocument>) {}

    async readAll(): Promise<Crawl[]> {
        return await this.crawlModel.find().exec();
    }

}