CREATE TABLE IF NOT EXISTS "products" (
  "id" int PRIMARY KEY,
  "name" VARCHAR(50),
  "type" VARCHAR(50),
  "rank" INT,
  "cost" INT
);

CREATE TABLE IF NOT EXISTS "customers" (
  "id" int PRIMARY KEY,
  "basket_id" int,
  "name" VARCHAR(50),
  "email" VARCHAR(50),
  "phone_number" VARCHAR(50),
  "location" VARCHAR(50),
  "payment" int
);

CREATE TABLE IF NOT EXISTS "basket" (
  "id" int PRIMARY KEY,
  "cost" INT,
  "counter" INT,
  "products_id" INT
);

CREATE TABLE IF NOT EXISTS "company" (
  "id" int PRIMARY KEY,
  "country" VARCHAR(50),
  "products_id" INT
);