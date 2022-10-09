import { Prop, Schema, SchemaFactory } from "@nestjs/mongoose";
import { Document } from "mongoose";

export type CrawlDocument = Crawl & Document;

@Schema()
export class Crawl {

    @Prop()
    name: string;

    @Prop()
    author: string;

    @Prop()
    publishYear: number;
}

export const CrawlSchema = SchemaFactory.createForClass(Crawl);