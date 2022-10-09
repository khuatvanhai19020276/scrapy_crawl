import { Body, Controller, Delete, Get, HttpStatus, Param, Post, Put, Render, Res } from "@nestjs/common";
import { Crawl } from "src/schemas/crawl.schema";
import { CrawlService } from "src/services/crawl.service";

@Controller('crawls')
export class CrawlController {
    constructor(private readonly crawlService: CrawlService){}

    @Get()
    async fetchAll(@Res() response) {
        const crawls = await this.crawlService.readAll();
        return response.status(HttpStatus.OK).json({
            crawls
        })
    }
    
}