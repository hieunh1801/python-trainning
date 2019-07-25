CREATE TYPE "roles" AS ENUM (
  'admin',
  'manager',
  'employee',
  'none'
);

CREATE TYPE "resource_tables" AS ENUM (
  'file',
  'news',
  'basket',
  'topic',
  'report'
);

CREATE TYPE "privilege_on_resource" AS ENUM (
  'view',
  'edit',
  'owner'
);

CREATE TABLE "user" (
  "user_id" SERIAL PRIMARY KEY,
  "role" "roles",
  "superior_id" int,
  "username" char(32) UNIQUE,
  "password" char(32),
  "fullname" text,
  "dob" date,
  "address" text,
  "phonenumber" char(15),
  "email" char(50)
);

CREATE TABLE "resource" (
  "resource_id" SERIAL PRIMARY KEY,
  "table_name" "resource_tables",
  "specific_id" int,
  "required_role" "roles",
  "date_created" date
);

CREATE TABLE "user_resource" (
  "user_resource_id" SERIAL PRIMARY KEY,
  "user_id" int,
  "resource_id" int,
  "privilege" "privilege_on_resource"
);

CREATE TABLE "user_group" (
  "user_group_id" SERIAL PRIMARY KEY,
  "owner_id" int,
  "group_name" text
);

CREATE TABLE "user_group_detail" (
  "detail_id" int PRIMARY KEY,
  "user_group_id" int,
  "user_id" int
);

CREATE TABLE "resource_group" (
  "resrouce_group_id" SERIAL PRIMARY KEY,
  "group_name" text,
  "owner_id" int
);

CREATE TABLE "resource_group_detail" (
  "detail_id" SERIAL PRIMARY KEY,
  "resource_group_id" int,
  "resource_id" int
);

CREATE TABLE "file" (
  "file_id" SERIAL PRIMARY KEY,
  "type" char(10),
  "url" varchar(50)
);

CREATE TABLE "news" (
  "news_id" SERIAL PRIMARY KEY,
  "title" text,
  "summarize" text,
  "content" text
);

CREATE TABLE "basket" (
  "basket_id" SERIAL PRIMARY KEY,
  "basket_name" text
);

CREATE TABLE "basket_detail" (
  "detail_id" SERIAL PRIMARY KEY,
  "basket_id" int,
  "news_id" int
);

CREATE TABLE "report" (
  "report_id" SERIAL PRIMARY KEY,
  "higher_report_id" int,
  "numerical_order" int,
  "content" text
);

ALTER TABLE "user_resource" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("user_id");

ALTER TABLE "user_resource" ADD FOREIGN KEY ("resource_id") REFERENCES "resource" ("resource_id");

ALTER TABLE "user_group_detail" ADD FOREIGN KEY ("user_group_id") REFERENCES "user_group" ("user_group_id");

ALTER TABLE "resource_group_detail" ADD FOREIGN KEY ("resource_group_id") REFERENCES "resource_group" ("resrouce_group_id");

ALTER TABLE "user_group_detail" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("user_id");

ALTER TABLE "resource_group_detail" ADD FOREIGN KEY ("resource_id") REFERENCES "resource" ("resource_id");

ALTER TABLE "basket_detail" ADD FOREIGN KEY ("basket_id") REFERENCES "basket" ("basket_id");

ALTER TABLE "basket_detail" ADD FOREIGN KEY ("news_id") REFERENCES "news" ("news_id");

ALTER TABLE "user" ADD FOREIGN KEY ("superior_id") REFERENCES "user" ("user_id");

ALTER TABLE "user_group" ADD FOREIGN KEY ("owner_id") REFERENCES "user" ("user_id");

ALTER TABLE "resource_group" ADD FOREIGN KEY ("owner_id") REFERENCES "user" ("user_id");

ALTER TABLE "report" ADD FOREIGN KEY ("higher_report_id") REFERENCES "report" ("report_id");