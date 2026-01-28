# Bloomsbury Tech Data Dictionary

Generated on: 2026-01-28 11:38:47

# Database: `sothebys`

## Table: `sothebys.artist_mappings`

**Row Count:** 2,103

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `artist_id` | Int64 | 100.0% | 2,103 | 99999 | 102101 | Avg: 101050.00 |
| `artist_name` | String | 100.0% | 2,103 | - | - | Xu, Lei, Yektai, Manouch..., Yu, Fei'an |
| `lot_count` | Int32 | 100.0% | 117 | 0 | 1648 | Avg: 17.36 |
| `is_rare` | UInt8 | 100.0% | 2 | 0 | 1 | Avg: 0.00 |
| `created_at` | DateTime | 100.0% | 2 | 2026-01-21 16:29:19 | 2026-01-25 20:29:47 | - |

---

## Table: `sothebys.auctions`

**Row Count:** 2,394

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_uuid` | String | 100.0% | 2,394 | - | - | 7ee69b7e-aef7-4..., 80def2d1-26df-4..., 81395394-4fc7-4... |
| `title` | String | 100.0% | 1,626 | - | - | Contemporary Cu..., Watches Weekly ..., Master Sculptur... |
| `sap_sale_number` | Nullable(String) | 100.0% | 2,394 | - | - | N11806, HK0962, PF2228 |
| `department` | Nullable(String) | 100.0% | 95 | - | - | Wine, Contemporary Ar..., Chinese Works o... |
| `category` | Nullable(String) | 0.0% | 0 | - | - |  |
| `currency` | Nullable(String) | 100.0% | 7 | - | - | USD, GBP, EUR |
| `auction_type` | Nullable(String) | 100.0% | 2 | - | - | Timed, Live |
| `state` | Nullable(String) | 100.0% | 1 | - | - | Closed |
| `location` | Nullable(String) | 100.0% | 13 | - | - | New York, London, Hong Kong |
| `timezone` | Nullable(String) | 100.0% | 10 | - | - | America/New_Yor..., Europe/London, Hongkong |
| `date_opens` | Nullable(DateTime) | 0.1% | 3 | 2018-05-07 14:00:55 | 2018-05-17 14:00:57 | - |
| `date_starts_closing` | Nullable(DateTime) | 0.5% | 12 | 2018-05-24 17:00:57 | 2025-12-04 12:00:59 | - |
| `date_closed` | Nullable(DateTime) | 98.2% | 2,350 | 2018-05-24 17:55:49 | 2026-01-08 19:39:47 | - |
| `date_published` | Nullable(DateTime) | 99.9% | 2,392 | 2018-04-30 11:26:44 | 2025-12-05 15:50:04 | - |
| `date_range` | Nullable(String) | 0.0% | 0 | - | - |  |
| `time` | Nullable(String) | 0.0% | 0 | - | - |  |
| `slug_year` | Nullable(String) | 100.0% | 8 | - | - | 2020, 2021, 2023 |
| `slug_name` | Nullable(String) | 100.0% | 1,858 | - | - | contemporary-di..., original-film-p..., sculpture-from-... |
| `url` | Nullable(String) | 100.0% | 2,394 | - | - | https://www.sot..., https://www.sot..., https://www.sot... |
| `image_url` | Nullable(String) | 0.0% | 0 | - | - |  |
| `overview` | Nullable(String) | 100.0% | 2,380 | - | - | <p>2024年新年伊始，蘇富..., <p>Lead by an e..., <p>Sotheby’s is... |
| `conditions_of_sale` | Nullable(String) | 100.0% | 1,390 | - | - | <p>Please revie..., <p>Please revie..., <p>Please revie... |
| `sale_total` | Nullable(Float64) | 0.0% | 0 | - | - | - |
| `lot_count` | Nullable(Int32) | 0.0% | 0 | - | - | - |
| `scraped_at` | DateTime | 100.0% | 138 | 2026-01-26 02:58:57 | 2026-01-26 03:01:19 | - |
| `created_at` | DateTime | 100.0% | 2,394 | 2026-01-15 14:52:27 | 2026-01-16 01:12:10 | - |
| `updated_at` | DateTime | 100.0% | 2,394 | 2026-01-15 15:06:00 | 2026-01-16 01:12:10 | - |

---

## Table: `sothebys.bronze_lot_pages`

**Row Count:** 99,745

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 85,615 | - | - | fffa9072-dc7e-4..., ffef28a9-9b73-4..., ffea6a48-3a5b-4... |
| `auction_uuid` | String | 100.0% | 2,382 | - | - | f476d7ed-9031-4..., e10e4bae-0c80-4..., ee65f182-1de5-4... |
| `url` | String | 100.0% | 85,354 | - | - | https://www.sot..., https://www.sot..., https://www.sot... |
| `raw_html` | String | 100.0% | 1 | - | - |  |
| `content_hash` | String | 100.0% | 85,645 | - | - | 0dc8b0c6b879163..., 43ff5f001272b00..., c4453351959b232... |
| `http_status` | Int32 | 100.0% | 1 | 200 | 200 | Avg: 200.00 |
| `scraped_at` | DateTime | 100.0% | 40,950 | 2026-01-21 12:59:08 | 2026-01-25 07:39:43 | - |
| `page_size_bytes` | Int64 | 100.0% | 75,424 | 252118 | 1731886 | Avg: 1125257.95 |

---

## Table: `sothebys.fx_rates`

**Row Count:** 16,854

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `rate_date` | Date | 100.0% | 2,809 | 2018-05-02 | 2026-01-08 | - |
| `currency` | String | 100.0% | 6 | - | - | CHF, CNY, EUR |
| `rate_to_usd` | Float64 | 100.0% | 8,065 | 0.12738691226863352 | 1.421201483734349 | Avg: 0.75 |
| `fetched_at` | DateTime | 100.0% | 1 | 2026-01-21 17:03:34 | 2026-01-21 17:03:34 | - |

---

## Table: `sothebys.gold_features`

**Row Count:** 88,620

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 88,909 | - | - | ffea6a48-3a5b-4..., ffef28a9-9b73-4..., fff56707-ba4a-4... |
| `surface_area_cm2` | Nullable(Float64) | 45.9% | 22,943 | 0.6 | 601261.0800000001 | Avg: 7195.48 |
| `log_hammer_price` | Nullable(Float64) | 33.3% | 12,943 | -0.02644717001484828 | 16.860032995687696 | Avg: 8.83 |
| `log_surface_area` | Nullable(Float64) | 45.9% | 22,742 | -0.5108256237659907 | 13.306784528506737 | Avg: 7.83 |
| `artist_id` | Nullable(Int64) | 66.2% | 2,103 | 99999 | 102101 | Avg: 100657.00 |
| `is_rare_artist` | UInt8 | 100.0% | 2 | 0 | 1 | Avg: 0.25 |
| `vital_status` | Nullable(String) | 100.0% | 3 | - | - | alive, dead, unknown |
| `computed_at` | DateTime | 100.0% | 1 | 2026-01-25 20:29:47 | 2026-01-25 20:29:47 | - |

---

## Table: `sothebys.lots`

**Row Count:** 99,971

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 100,423 | - | - | ffdd1859-de05-4..., ffe0a228-43b0-4..., ffea6a48-3a5b-4... |
| `auction_uuid` | String | 100.0% | 2,394 | - | - | f476d7ed-9031-4..., e10e4bae-0c80-4..., ee65f182-1de5-4... |
| `lot_number` | Nullable(Int32) | 100.0% | 3,651 | 1 | 9901 | Avg: 668.77 |
| `title` | Nullable(String) | 100.0% | 87,262 | - | - | Untitled, EDUARDO LEÓN GA..., Guerrier assis,... |
| `subtitle` | Nullable(String) | 2.3% | 1,836 | - | - |  , 2018 Release, In Original Woo... |
| `creator` | Nullable(String) | 39.1% | 11,901 | - | - | Pablo Picasso, Tiffany Studios, Albrecht Dürer |
| `slug` | Nullable(String) | 100.0% | 88,790 | - | - | lynn-chadwick-p..., joan-mitchell-u..., chateau-latour-... |
| `estimate_low` | Nullable(Float64) | 99.4% | 297 | 10 | 255000000 | Avg: 243671.70 |
| `estimate_high` | Nullable(Float64) | 99.4% | 332 | 20 | 350000000 | Avg: 363479.11 |
| `tags` | Nullable(String) | 100.0% | 2 | - | - | [], ["NoReserve"] |
| `accepts_crypto` | UInt8 | 100.0% | 2 | 0 | 1 | Avg: 0.01 |
| `withdrawn_state` | Nullable(String) | 100.0% | 2 | - | - | NotAffected, UnWithdrawn |
| `session_id` | Nullable(Int32) | 100.0% | 2 | 0 | 1 | Avg: 0.00 |
| `created_at` | DateTime | 100.0% | 2,448 | 2026-01-15 14:52:27 | 2026-01-16 01:12:10 | - |
| `updated_at` | DateTime | 100.0% | 2,448 | 2026-01-15 15:06:00 | 2026-01-16 01:12:10 | - |

---

## Table: `sothebys.raw_auctions`

**Row Count:** 2,390

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_uuid` | String | 100.0% | 2,390 | - | - | fc0130cc-cb1e-4..., fc94ac90-f97b-4..., fd08f7c4-a5c9-4... |
| `sap_sale_number` | Nullable(String) | 100.0% | 2,390 | - | - | HK1390, N10410, HK1147 |
| `date_starts_closing` | Nullable(String) | 0.0% | 0 | - | - |  |
| `currency` | Nullable(String) | 100.0% | 7 | - | - | USD, GBP, EUR |
| `lot_count` | Nullable(Int32) | 100.0% | 48 | 1 | 48 | Avg: 41.72 |

---

## Table: `sothebys.raw_lots`

**Row Count:** 99,742

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 81,837 | - | - | 65e6b76b-e2da-4..., 65e95dea-535b-4..., 65eee18d-c62c-4... |
| `auction_uuid` | Nullable(String) | 100.0% | 2,380 | - | - | 709c0b36-46dd-4..., 9700060c-2195-4..., 5624f12d-52ff-4... |
| `lot_number` | Nullable(String) | 7.0% | 1,151 | - | - | 34, 13, 6009 |
| `sap_sale_number` | Nullable(String) | 100.0% | 2,380 | - | - | L22102, L19132, N10719 |
| `slug` | Nullable(String) | 100.0% | 73,353 | - | - | hermitage-rouge..., chateau-lafite-..., loiseau-console |
| `title` | Nullable(String) | 100.0% | 72,148 | - | - | Untitled, SIR EDWARD COLE..., EDUARDO LEÓN GA... |
| `subtitle` | Nullable(String) | 2.3% | 1,506 | - | - |  , 2018 Release, In Original Woo... |
| `description_html` | Nullable(String) | 100.0% | 1 | - | - |  |
| `description_text` | Nullable(String) | 100.0% | 80,259 | - | - | Property from a..., 文徵明 千巖萬壑 設色金箋 扇..., Property of a G... |
| `creators_display` | Nullable(String) | 39.2% | 10,434 | - | - | Pablo Picasso, Tiffany Studios, Banksy |
| `designation_line` | Nullable(String) | 37.3% | 4,727 | - | - | Property from a..., Property from a..., Property from a... |
| `object_type` | Nullable(String) | 100.0% | 52 | - | - | Generic, Painting, Wine |
| `estimate_low` | Nullable(Float64) | 99.4% | 278 | 20 | 175000000 | Avg: 238672.91 |
| `estimate_high` | Nullable(Float64) | 99.4% | 312 | 30 | 235000000 | Avg: 355430.48 |
| `currency` | Nullable(String) | 100.0% | 7 | - | - | USD, GBP, EUR |
| `provenance` | Nullable(String) | 100.0% | 33,687 | - | - | , Acquired direct..., Studio Ghibli B... |
| `literature` | Nullable(String) | 100.0% | 15,640 | - | - | , A. Morassi, Des..., Franz Müller an... |
| `exhibition` | Nullable(String) | 100.0% | 11,152 | - | - | , Chicago, Richar..., Tehran, Iran, A... |
| `catalogue_note` | Nullable(String) | 100.0% | 17,110 | - | - | , “Rome remained ..., The turn of the... |
| `saleroom_notice` | Nullable(String) | 100.0% | 1,806 | - | - | , Please note tha..., This lot has an... |
| `session_date` | Nullable(String) | 100.0% | 2,224 | - | - | 2024-12-18T15:1..., 2019-04-10T13:0..., 2024-11-22T17:0... |
| `symbols_json` | Nullable(String) | 40.9% | 517 | - | - | [{"symbol": "Re..., [{"symbol": "Ar..., [{"symbol": "VA... |
| `images_json` | Nullable(String) | 100.0% | 81,459 | - | - | [{"title": "Ras..., [{"title": "065..., [{"title": "DE2... |
| `prev_lot_uuid` | Nullable(String) | 97.6% | 80,003 | - | - | 09e95ece-4108-4..., 759a0a92-f1b2-4..., 80ed1238-3fbf-4... |
| `next_lot_uuid` | Nullable(String) | 99.4% | 81,364 | - | - | 163a7d18-ba11-4..., 0e37795c-d245-4..., 3f1dfc6e-cc2c-4... |
| `raw_json` | Nullable(String) | 100.0% | 1 | - | - |  |
| `extracted_at` | Nullable(String) | 0.0% | 0 | - | - |  |

---

## Table: `sothebys.review_decisions`

**Row Count:** 12

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | Int64 | 100.0% | 12 | 1 | 18 | Avg: 9.42 |
| `lot_uuid` | String | 100.0% | 3 | - | - | 0002a26c-0730-4..., 0002407e-e0e9-4..., 0000b010-d97c-4... |
| `field_name` | String | 100.0% | 5 | - | - | artist_name, medium, artist_national... |
| `decision` | String | 100.0% | 3 | - | - | accept, reject, edit |
| `original_value` | Nullable(String) | 8.3% | 1 | - | - | c. 1569 |
| `corrected_value` | Nullable(String) | 8.3% | 1 | - | - | oil on canvas |
| `original_confidence` | Nullable(Float64) | 100.0% | 2 | 0 | 1 | Avg: 0.08 |
| `reviewed_at` | DateTime | 100.0% | 3 | 2026-01-21 13:54:59 | 2026-01-21 14:14:46 | - |

---

## Table: `sothebys.review_queue`

**Row Count:** 3

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 3 | - | - | 0000b010-d97c-4..., 0002407e-e0e9-4..., 0002a26c-0730-4... |
| `queue_position` | Int32 | 100.0% | 3 | 0 | 2 | Avg: 1.00 |
| `reason` | String | 100.0% | 1 | - | - | low_confidence |
| `added_at` | DateTime | 100.0% | 1 | 2026-01-21 14:30:56 | 2026-01-21 14:30:56 | - |

---

## Table: `sothebys.sales`

**Row Count:** 99,971

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 79,484 | - | - | ffea6a48-3a5b-4..., ffef28a9-9b73-4..., fff56707-ba4a-4... |
| `is_closed` | UInt8 | 100.0% | 1 | 1 | 1 | Avg: 1.00 |
| `reserve_met` | Nullable(UInt8) | 100.0% | 2 | 0 | 1 | Avg: 0.80 |
| `num_bids` | Nullable(Int32) | 39.9% | 86 | 1 | 107 | Avg: 10.91 |
| `starting_bid` | Nullable(Float64) | 100.0% | 327 | 1 | 200000000 | Avg: 237895.45 |
| `hammer_price` | Nullable(Float64) | 39.9% | 208 | 1 | 21000000 | Avg: 34728.17 |
| `final_price` | Nullable(Float64) | 39.9% | 725 | 1 | 24393000 | Avg: 43502.94 |
| `currency` | Nullable(String) | 39.9% | 7 | - | - | USD, GBP, EUR |
| `is_sold` | UInt8 | 100.0% | 2 | 0 | 1 | Avg: 0.39 |
| `bid_method` | Nullable(String) | 100.0% | 4 | - | - | Online, Advanced, Absentee |
| `closing_time` | Nullable(DateTime) | 15.6% | 12,317 | 2018-05-24 17:11:57 | 2026-01-08 14:20:49 | - |
| `created_at` | DateTime | 100.0% | 1,910 | 2026-01-15 14:52:27 | 2026-01-15 22:42:12 | - |
| `updated_at` | DateTime | 100.0% | 1,910 | 2026-01-15 15:06:00 | 2026-01-15 22:42:12 | - |

---

## Table: `sothebys.silver_extractions`

**Row Count:** 88,620

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 88,909 | - | - | ffea6a48-3a5b-4..., ffef28a9-9b73-4..., fff56707-ba4a-4... |
| `auction_uuid` | String | 100.0% | 2,386 | - | - | f476d7ed-9031-4..., ee65f182-1de5-4..., efa89cc4-6ccb-4... |
| `extracted_at` | DateTime | 100.0% | 16,635 | 2026-01-21 18:10:29 | 2026-01-25 19:02:17 | - |
| `extraction_version` | String | 100.0% | 1 | - | - | v1 |
| `artist_name` | Nullable(String) | 66.2% | 17,768 | - | - | Picasso, Pablo, Tiffany Studios, Garrido, Eduard... |
| `artist_nationality` | Nullable(String) | 15.7% | 320 | - | - | French, Italian, Chinese |
| `artist_birth_year` | Nullable(Int32) | 45.9% | 632 | 1000 | 2015 | Avg: 1877.69 |
| `artist_death_year` | Nullable(Int32) | 32.9% | 622 | 1000 | 2100 | Avg: 1918.73 |
| `artist_name_confidence` | Float64 | 100.0% | 10 | 0 | 1 | Avg: 0.65 |
| `artist_nationality_confidence` | Float64 | 100.0% | 5 | 0 | 1 | Avg: 0.14 |
| `artist_dates_confidence` | Float64 | 100.0% | 8 | 0 | 1 | Avg: 0.46 |
| `height_cm` | Nullable(Float64) | 52.6% | 2,222 | 0.6 | 1000 | Avg: 66.28 |
| `width_cm` | Nullable(Float64) | 46.0% | 2,259 | 0.3 | 1000 | Avg: 68.39 |
| `depth_cm` | Nullable(Float64) | 5.6% | 717 | 0.3 | 938.1 | Avg: 35.27 |
| `dimensions_confidence` | Float64 | 100.0% | 2 | 0 | 1 | Avg: 0.53 |
| `medium` | Nullable(String) | 88.1% | 12,198 | - | - | oil, wine, bronze |
| `support` | Nullable(String) | 58.8% | 3,747 | - | - | paper, canvas, panel |
| `medium_confidence` | Float64 | 100.0% | 6 | 0 | 1 | Avg: 0.87 |
| `creation_year` | Nullable(Int32) | 77.6% | 802 | 1000 | 2100 | Avg: 1908.24 |
| `creation_is_approximate` | UInt8 | 100.0% | 2 | 0 | 1 | Avg: 0.45 |
| `creation_period` | Nullable(String) | 14.1% | 2,057 | - | - | 19th century, 18th century, 17th century |
| `creation_confidence` | Float64 | 100.0% | 6 | 0 | 1 | Avg: 0.91 |
| `creation_source` | String | 100.0% | 2 | - | - | regex, llm |
| `tax_bonded` | UInt8 | 100.0% | 1 | 0 | 0 | Avg: 0.00 |
| `tax_vat` | UInt8 | 100.0% | 1 | 0 | 0 | Avg: 0.00 |
| `is_guaranteed` | UInt8 | 100.0% | 1 | 0 | 0 | Avg: 0.00 |
| `regime_1031` | UInt8 | 100.0% | 1 | 0 | 0 | Avg: 0.00 |
| `hammer_price_usd` | Nullable(Float64) | 33.3% | 12,954 | 0.9738994935722634 | 21000000 | Avg: 22680.08 |
| `price_normalized_at` | Nullable(DateTime) | 100.0% | 7 | 2026-01-25 20:12:07 | 2026-01-25 20:29:39 | - |
| `enriched_at` | Nullable(DateTime) | 100.0% | 1,335 | 2026-01-25 20:06:11 | 2026-01-25 20:28:43 | - |
| `raw_description` | Nullable(String) | 100.0% | 87,370 | - | - | 張大千 行書「老子猶龍」 水墨..., Marten van Clev..., Euclide La pers... |
| `extraction_error` | Nullable(String) | 0.0% | 0 | - | - |  |

---

## Table: `sothebys.v_gold_with_artist`

**Row Count:** 88,620

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 88,909 | - | - | ffea6a48-3a5b-4..., ffef28a9-9b73-4..., fff56707-ba4a-4... |
| `surface_area_cm2` | Nullable(Float64) | 45.9% | 22,943 | 0.6 | 601261.0800000001 | Avg: 7195.48 |
| `log_hammer_price` | Nullable(Float64) | 33.3% | 12,943 | -0.02644717001484828 | 16.860032995687696 | Avg: 8.83 |
| `log_surface_area` | Nullable(Float64) | 45.9% | 22,742 | -0.5108256237659907 | 13.306784528506737 | Avg: 7.83 |
| `artist_id` | Nullable(Int64) | 66.2% | 2,103 | 99999 | 102101 | Avg: 100657.00 |
| `is_rare_artist` | UInt8 | 100.0% | 2 | 0 | 1 | Avg: 0.25 |
| `vital_status` | Nullable(String) | 100.0% | 3 | - | - | alive, dead, unknown |
| `computed_at` | DateTime | 100.0% | 1 | 2026-01-25 20:29:47 | 2026-01-25 20:29:47 | - |
| `artist_name` | String | 100.0% | 2,104 | - | - | , __RARE_ARTIST__, Picasso, Pablo |
| `artist_lot_count` | Int32 | 100.0% | 117 | 0 | 1648 | Avg: 60.25 |

---

## Table: `sothebys.v_lot_with_sales`

**Row Count:** 120,942

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `l.lot_uuid` | String | 100.0% | 100,423 | - | - | ffd0f592-3e4a-4..., ffd2346a-84e9-4..., ffdd1859-de05-4... |
| `l.auction_uuid` | String | 100.0% | 2,394 | - | - | f476d7ed-9031-4..., ee65f182-1de5-4..., cbc4def9-e55b-4... |
| `lot_number` | Nullable(Int32) | 100.0% | 3,651 | 1 | 9901 | Avg: 678.66 |
| `l.title` | Nullable(String) | 100.0% | 87,262 | - | - | Untitled, Circle of Jacop..., A FABERGÉ GEM-S... |
| `creator` | Nullable(String) | 39.9% | 11,901 | - | - | Pablo Picasso, Tiffany Studios, Albrecht Dürer |
| `estimate_low` | Nullable(Float64) | 99.3% | 297 | 10 | 255000000 | Avg: 247954.86 |
| `estimate_high` | Nullable(Float64) | 99.3% | 332 | 20 | 350000000 | Avg: 370185.56 |
| `hammer_price` | Nullable(Float64) | 33.0% | 208 | 1 | 21000000 | Avg: 34728.17 |
| `final_price` | Nullable(Float64) | 33.0% | 725 | 1 | 24393000 | Avg: 43502.94 |
| `is_sold` | UInt8 | 100.0% | 2 | 0 | 1 | Avg: 0.32 |
| `num_bids` | Nullable(Int32) | 33.0% | 86 | 1 | 107 | Avg: 10.91 |
| `auction_title` | String | 100.0% | 1,626 | - | - | Contemporary Di..., Fine Jewels, Modern & Contem... |
| `department` | Nullable(String) | 99.9% | 95 | - | - | Wine, Contemporary Ar..., Books & Manuscr... |
| `location` | Nullable(String) | 99.9% | 13 | - | - | New York, London, Hong Kong |
| `date_starts_closing` | Nullable(DateTime) | 0.6% | 12 | 2018-05-24 17:00:57 | 2025-12-04 12:00:59 | - |

---

## Table: `sothebys.v_silver_with_auction`

**Row Count:** 88,620

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 88,909 | - | - | ffea6a48-3a5b-4..., ffef28a9-9b73-4..., fff56707-ba4a-4... |
| `auction_uuid` | String | 100.0% | 2,386 | - | - | f476d7ed-9031-4..., ee65f182-1de5-4..., efa89cc4-6ccb-4... |
| `extracted_at` | DateTime | 100.0% | 16,635 | 2026-01-21 18:10:29 | 2026-01-25 19:02:17 | - |
| `extraction_version` | String | 100.0% | 1 | - | - | v1 |
| `artist_name` | Nullable(String) | 66.2% | 17,768 | - | - | Picasso, Pablo, Tiffany Studios, Garrido, Eduard... |
| `artist_nationality` | Nullable(String) | 15.7% | 320 | - | - | French, Italian, Chinese |
| `artist_birth_year` | Nullable(Int32) | 45.9% | 632 | 1000 | 2015 | Avg: 1877.69 |
| `artist_death_year` | Nullable(Int32) | 32.9% | 622 | 1000 | 2100 | Avg: 1918.73 |
| `artist_name_confidence` | Float64 | 100.0% | 10 | 0 | 1 | Avg: 0.65 |
| `artist_nationality_confidence` | Float64 | 100.0% | 5 | 0 | 1 | Avg: 0.14 |
| `artist_dates_confidence` | Float64 | 100.0% | 8 | 0 | 1 | Avg: 0.46 |
| `height_cm` | Nullable(Float64) | 52.6% | 2,222 | 0.6 | 1000 | Avg: 66.28 |
| `width_cm` | Nullable(Float64) | 46.0% | 2,259 | 0.3 | 1000 | Avg: 68.39 |
| `depth_cm` | Nullable(Float64) | 5.6% | 717 | 0.3 | 938.1 | Avg: 35.27 |
| `dimensions_confidence` | Float64 | 100.0% | 2 | 0 | 1 | Avg: 0.53 |
| `medium` | Nullable(String) | 88.1% | 12,198 | - | - | oil, wine, bronze |
| `support` | Nullable(String) | 58.8% | 3,747 | - | - | paper, canvas, panel |
| `medium_confidence` | Float64 | 100.0% | 6 | 0 | 1 | Avg: 0.87 |
| `creation_year` | Nullable(Int32) | 77.6% | 802 | 1000 | 2100 | Avg: 1908.24 |
| `creation_is_approximate` | UInt8 | 100.0% | 2 | 0 | 1 | Avg: 0.45 |
| `creation_period` | Nullable(String) | 14.1% | 2,057 | - | - | 19th century, 18th century, 17th century |
| `creation_confidence` | Float64 | 100.0% | 6 | 0 | 1 | Avg: 0.91 |
| `creation_source` | String | 100.0% | 2 | - | - | regex, llm |
| `tax_bonded` | UInt8 | 100.0% | 1 | 0 | 0 | Avg: 0.00 |
| `tax_vat` | UInt8 | 100.0% | 1 | 0 | 0 | Avg: 0.00 |
| `is_guaranteed` | UInt8 | 100.0% | 1 | 0 | 0 | Avg: 0.00 |
| `regime_1031` | UInt8 | 100.0% | 1 | 0 | 0 | Avg: 0.00 |
| `hammer_price_usd` | Nullable(Float64) | 33.3% | 12,954 | 0.9738994935722634 | 21000000 | Avg: 22680.08 |
| `price_normalized_at` | Nullable(DateTime) | 100.0% | 7 | 2026-01-25 20:12:07 | 2026-01-25 20:29:39 | - |
| `enriched_at` | Nullable(DateTime) | 100.0% | 1,335 | 2026-01-25 20:06:11 | 2026-01-25 20:28:43 | - |
| `raw_description` | Nullable(String) | 100.0% | 87,370 | - | - | 張大千 行書「老子猶龍」 水墨..., Marten van Clev..., Euclide La pers... |
| `extraction_error` | Nullable(String) | 0.0% | 0 | - | - |  |
| `auction_title` | String | 100.0% | 1,618 | - | - | Contemporary Di..., Fine Jewels, Modern & Contem... |
| `department` | Nullable(String) | 99.9% | 94 | - | - | Wine, Contemporary Ar..., Books & Manuscr... |
| `location` | Nullable(String) | 99.9% | 12 | - | - | New York, London, Hong Kong |
| `date_starts_closing` | Nullable(DateTime) | 0.6% | 12 | 2018-05-24 17:00:57 | 2025-12-04 12:00:59 | - |

---

# Database: `christies`

## Table: `christies.auctions`

**Row Count:** 0

*Table is empty.*

---

## Table: `christies.bronze_auction_list_pages`

**Row Count:** 0

*Table is empty.*

---

## Table: `christies.bronze_auction_pages`

**Row Count:** 0

*Table is empty.*

---

## Table: `christies.bronze_lot_pages`

**Row Count:** 0

*Table is empty.*

---

## Table: `christies.gold_features`

**Row Count:** 0

*Table is empty.*

---

## Table: `christies.lots`

**Row Count:** 0

*Table is empty.*

---

## Table: `christies.raw_auctions`

**Row Count:** 0

*Table is empty.*

---

## Table: `christies.raw_lots`

**Row Count:** 0

*Table is empty.*

---

## Table: `christies.silver_extractions`

**Row Count:** 0

*Table is empty.*

---

## Table: `christies.v_auction_stats`

**Row Count:** 0

*Table is empty.*

---

## Table: `christies.v_lots_enriched`

**Row Count:** 0

*Table is empty.*

---

# Database: `auction_19th_century_american_and_western_art`

## Table: `auction_19th_century_american_and_western_art.auctions`

**Row Count:** 1

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_uuid` | String | 100.0% | 1 | - | - | 30962 |
| `title` | String | 100.0% | 1 | - | - | 19th Century Am... |
| `sap_sale_number` | Nullable(String) | 0.0% | 0 | - | - |  |
| `department` | Nullable(String) | 0.0% | 0 | - | - |  |
| `category` | Nullable(String) | 0.0% | 0 | - | - |  |
| `currency` | Nullable(String) | 0.0% | 0 | - | - |  |
| `auction_type` | Nullable(String) | 0.0% | 0 | - | - |  |
| `state` | Nullable(String) | 0.0% | 0 | - | - |  |
| `location` | Nullable(String) | 0.0% | 0 | - | - |  |
| `timezone` | Nullable(String) | 0.0% | 0 | - | - |  |
| `date_opens` | Nullable(DateTime) | 0.0% | 0 | - | - | - |
| `date_starts_closing` | Nullable(DateTime) | 0.0% | 0 | - | - | - |
| `date_closed` | Nullable(DateTime) | 0.0% | 0 | - | - | - |
| `date_published` | Nullable(DateTime) | 0.0% | 0 | - | - | - |
| `date_range` | Nullable(String) | 0.0% | 0 | - | - |  |
| `time` | Nullable(String) | 0.0% | 0 | - | - |  |
| `slug_year` | Nullable(String) | 0.0% | 0 | - | - |  |
| `slug_name` | Nullable(String) | 0.0% | 0 | - | - |  |
| `url` | Nullable(String) | 100.0% | 1 | - | - | https://www.chr... |
| `image_url` | Nullable(String) | 0.0% | 0 | - | - |  |
| `overview` | Nullable(String) | 0.0% | 0 | - | - |  |
| `conditions_of_sale` | Nullable(String) | 0.0% | 0 | - | - |  |
| `sale_total` | Nullable(Float64) | 0.0% | 0 | - | - | - |
| `lot_count` | Nullable(Int32) | 0.0% | 0 | - | - | - |
| `scraped_at` | DateTime | 100.0% | 1 | 2026-01-28 05:18:49 | 2026-01-28 05:18:49 | - |
| `created_at` | DateTime | 100.0% | 1 | 2026-01-28 05:18:49 | 2026-01-28 05:18:49 | - |
| `updated_at` | DateTime | 100.0% | 1 | 2026-01-28 05:18:49 | 2026-01-28 05:18:49 | - |

---

## Table: `auction_19th_century_american_and_western_art.lot_images`

**Row Count:** 517

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_id` | String | 100.0% | 1 | - | - | 30962 |
| `lot_id` | String | 100.0% | 110 | - | - | 6570659, 6570676, 6570642 |
| `image_url` | String | 100.0% | 408 | - | - | https://www.chr..., https://www.chr..., https://www.chr... |
| `position` | UInt16 | 100.0% | 5 | 1 | 5 | Avg: 2.87 |
| `fetched_at` | DateTime | 100.0% | 52 | 2026-01-28 04:18:49 | 2026-01-28 04:19:40 | - |

---

## Table: `auction_19th_century_american_and_western_art.lots`

**Row Count:** 110

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 110 | - | - | 6570676, 6570618, 6570641 |
| `auction_uuid` | String | 100.0% | 1 | - | - | 30962 |
| `lot_number` | Nullable(Int32) | 100.0% | 110 | 401 | 511 | Avg: 456.41 |
| `title` | Nullable(String) | 100.0% | 109 | - | - | The Last Drop, Indian Caravan ..., Chinese Figure ... |
| `subtitle` | Nullable(String) | 0.0% | 0 | - | - |  |
| `creator` | Nullable(String) | 100.0% | 109 | - | - | JOHN GEORGE BRO..., JOSEPH MORVILLE..., THOMAS WORTHING... |
| `slug` | Nullable(String) | 0.0% | 0 | - | - |  |
| `estimate_low` | Nullable(Float64) | 0.9% | 1 | 12126362000 | 12126362000 | Avg: 12126362000.00 |
| `estimate_high` | Nullable(Float64) | 0.0% | 0 | - | - | - |
| `tags` | Nullable(String) | 0.0% | 0 | - | - |  |
| `accepts_crypto` | UInt8 | 100.0% | 1 | 0 | 0 | Avg: 0.00 |
| `withdrawn_state` | Nullable(String) | 35.5% | 1 | - | - | sold |
| `session_id` | Nullable(Int32) | 0.0% | 0 | - | - | - |
| `created_at` | DateTime | 100.0% | 1 | 2026-01-28 05:19:42 | 2026-01-28 05:19:42 | - |
| `updated_at` | DateTime | 100.0% | 1 | 2026-01-28 05:19:42 | 2026-01-28 05:19:42 | - |

---

## Table: `auction_19th_century_american_and_western_art.pages_raw`

**Row Count:** 121

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_id` | String | 100.0% | 1 | - | - | 30962 |
| `lot_id` | Nullable(String) | 90.9% | 110 | - | - | 6570676, 6570618, 6570641 |
| `url` | String | 100.0% | 121 | - | - | https://www.chr..., https://www.chr..., https://www.chr... |
| `final_url` | String | 100.0% | 121 | - | - | https://www.chr..., https://www.chr..., https://www.chr... |
| `page_type` | LowCardinality(String) | 100.0% | 2 | - | - | lot, listing |
| `http_status` | UInt16 | 100.0% | 1 | 200 | 200 | Avg: 200.00 |
| `fetched_at` | DateTime | 100.0% | 55 | 2026-01-28 04:18:49 | 2026-01-28 04:24:52 | - |
| `html` | String | 100.0% | 121 | - | - | 


<!DOCTYPE..., 


<!DOCTYPE..., 


<!DOCTYPE... |
| `html_sha256` | FixedString(64) | 100.0% | 121 | - | - | 8b37742b040e907..., 8ffcf02f24fc062..., d9fa6e61226debf... |
| `parse_version` | LowCardinality(String) | 100.0% | 1 | - | - | v1 |

---

# Database: `collector_connoisseur_the_max_n_berry_collections_american_art_d`

## Table: `collector_connoisseur_the_max_n_berry_collections_american_art_d.auctions`

**Row Count:** 1

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_uuid` | String | 100.0% | 1 | - | - | 31164 |
| `title` | String | 100.0% | 1 | - | - | COLLECTOR/CONNO... |
| `sap_sale_number` | Nullable(String) | 0.0% | 0 | - | - |  |
| `department` | Nullable(String) | 0.0% | 0 | - | - |  |
| `category` | Nullable(String) | 0.0% | 0 | - | - |  |
| `currency` | Nullable(String) | 0.0% | 0 | - | - |  |
| `auction_type` | Nullable(String) | 0.0% | 0 | - | - |  |
| `state` | Nullable(String) | 0.0% | 0 | - | - |  |
| `location` | Nullable(String) | 0.0% | 0 | - | - |  |
| `timezone` | Nullable(String) | 0.0% | 0 | - | - |  |
| `date_opens` | Nullable(DateTime) | 0.0% | 0 | - | - | - |
| `date_starts_closing` | Nullable(DateTime) | 0.0% | 0 | - | - | - |
| `date_closed` | Nullable(DateTime) | 0.0% | 0 | - | - | - |
| `date_published` | Nullable(DateTime) | 0.0% | 0 | - | - | - |
| `date_range` | Nullable(String) | 0.0% | 0 | - | - |  |
| `time` | Nullable(String) | 0.0% | 0 | - | - |  |
| `slug_year` | Nullable(String) | 0.0% | 0 | - | - |  |
| `slug_name` | Nullable(String) | 0.0% | 0 | - | - |  |
| `url` | Nullable(String) | 100.0% | 1 | - | - | https://www.chr... |
| `image_url` | Nullable(String) | 0.0% | 0 | - | - |  |
| `overview` | Nullable(String) | 0.0% | 0 | - | - |  |
| `conditions_of_sale` | Nullable(String) | 0.0% | 0 | - | - |  |
| `sale_total` | Nullable(Float64) | 0.0% | 0 | - | - | - |
| `lot_count` | Nullable(Int32) | 0.0% | 0 | - | - | - |
| `scraped_at` | DateTime | 100.0% | 1 | 2026-01-28 05:19:43 | 2026-01-28 05:19:43 | - |
| `created_at` | DateTime | 100.0% | 1 | 2026-01-28 05:19:43 | 2026-01-28 05:19:43 | - |
| `updated_at` | DateTime | 100.0% | 1 | 2026-01-28 05:19:43 | 2026-01-28 05:19:43 | - |

---

## Table: `collector_connoisseur_the_max_n_berry_collections_american_art_d.lot_images`

**Row Count:** 351

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_id` | String | 100.0% | 1 | - | - | 31164 |
| `lot_id` | String | 100.0% | 75 | - | - | 6570421, 6570413, 6570415 |
| `image_url` | String | 100.0% | 277 | - | - | https://www.chr..., https://www.chr..., https://www.chr... |
| `position` | UInt16 | 100.0% | 5 | 1 | 5 | Avg: 2.87 |
| `fetched_at` | DateTime | 100.0% | 33 | 2026-01-28 04:19:44 | 2026-01-28 04:20:16 | - |

---

## Table: `collector_connoisseur_the_max_n_berry_collections_american_art_d.lots`

**Row Count:** 75

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 75 | - | - | 6570410, 6570411, 6570413 |
| `auction_uuid` | String | 100.0% | 1 | - | - | 31164 |
| `lot_number` | Nullable(Int32) | 100.0% | 75 | 301 | 375 | Avg: 338.00 |
| `title` | Nullable(String) | 100.0% | 75 | - | - | Clam Diggers, N..., Taking in Sails..., Boating on the ... |
| `subtitle` | Nullable(String) | 0.0% | 0 | - | - |  |
| `creator` | Nullable(String) | 100.0% | 75 | - | - | JASPER FRANCIS ..., ROBERT KULICKE ..., ROBERT KULICKE ... |
| `slug` | Nullable(String) | 0.0% | 0 | - | - |  |
| `estimate_low` | Nullable(Float64) | 0.0% | 0 | - | - | - |
| `estimate_high` | Nullable(Float64) | 0.0% | 0 | - | - | - |
| `tags` | Nullable(String) | 0.0% | 0 | - | - |  |
| `accepts_crypto` | UInt8 | 100.0% | 1 | 0 | 0 | Avg: 0.00 |
| `withdrawn_state` | Nullable(String) | 40.0% | 1 | - | - | sold |
| `session_id` | Nullable(Int32) | 0.0% | 0 | - | - | - |
| `created_at` | DateTime | 100.0% | 1 | 2026-01-28 05:20:18 | 2026-01-28 05:20:18 | - |
| `updated_at` | DateTime | 100.0% | 1 | 2026-01-28 05:20:18 | 2026-01-28 05:20:18 | - |

---

## Table: `collector_connoisseur_the_max_n_berry_collections_american_art_d.pages_raw`

**Row Count:** 86

| Column | Type | Fill Rate | Unique Vals | Min | Max | Top Values / Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_id` | String | 100.0% | 1 | - | - | 31164 |
| `lot_id` | Nullable(String) | 87.2% | 75 | - | - | 6570410, 6570411, 6570413 |
| `url` | String | 100.0% | 86 | - | - | https://www.chr..., https://www.chr..., https://www.chr... |
| `final_url` | String | 100.0% | 86 | - | - | https://www.chr..., https://www.chr..., https://www.chr... |
| `page_type` | LowCardinality(String) | 100.0% | 2 | - | - | lot, listing |
| `http_status` | UInt16 | 100.0% | 1 | 200 | 200 | Avg: 200.00 |
| `fetched_at` | DateTime | 100.0% | 35 | 2026-01-28 04:19:44 | 2026-01-28 04:25:54 | - |
| `html` | String | 100.0% | 86 | - | - | 


<!DOCTYPE..., 


<!DOCTYPE..., 


<!DOCTYPE... |
| `html_sha256` | FixedString(64) | 100.0% | 86 | - | - | 0e84c609a7b4654..., 9adc6634d03a1be..., d6efeb818fd5a50... |
| `parse_version` | LowCardinality(String) | 100.0% | 1 | - | - | v1 |

---

