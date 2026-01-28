# Bloomsbury Tech Data Dictionary

Generated on: 2026-01-28 11:29:53

# Database: `sothebys`

## Table: `sothebys.artist_mappings`

**Row Count:** 2,103

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `artist_id` | Int64 | 100.0% | 2,103 | 99999 | 102101 |
| `artist_name` | String | 100.0% | 2,103 | - | - |
| `lot_count` | Int32 | 100.0% | 117 | 0 | 1648 |
| `is_rare` | UInt8 | 100.0% | 2 | 0 | 1 |
| `created_at` | DateTime | 100.0% | 2 | 2026-01-21 16:29:19 | 2026-01-25 20:29:47 |

---

## Table: `sothebys.auctions`

**Row Count:** 2,394

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_uuid` | String | 100.0% | 2,394 | - | - |
| `title` | String | 100.0% | 1,626 | - | - |
| `sap_sale_number` | Nullable(String) | 100.0% | 2,394 | - | - |
| `department` | Nullable(String) | 100.0% | 95 | - | - |
| `category` | Nullable(String) | 0.0% | 0 | - | - |
| `currency` | Nullable(String) | 100.0% | 7 | - | - |
| `auction_type` | Nullable(String) | 100.0% | 2 | - | - |
| `state` | Nullable(String) | 100.0% | 1 | - | - |
| `location` | Nullable(String) | 100.0% | 13 | - | - |
| `timezone` | Nullable(String) | 100.0% | 10 | - | - |
| `date_opens` | Nullable(DateTime) | 0.1% | 3 | 2018-05-07 14:00:55 | 2018-05-17 14:00:57 |
| `date_starts_closing` | Nullable(DateTime) | 0.5% | 12 | 2018-05-24 17:00:57 | 2025-12-04 12:00:59 |
| `date_closed` | Nullable(DateTime) | 98.2% | 2,350 | 2018-05-24 17:55:49 | 2026-01-08 19:39:47 |
| `date_published` | Nullable(DateTime) | 99.9% | 2,392 | 2018-04-30 11:26:44 | 2025-12-05 15:50:04 |
| `date_range` | Nullable(String) | 0.0% | 0 | - | - |
| `time` | Nullable(String) | 0.0% | 0 | - | - |
| `slug_year` | Nullable(String) | 100.0% | 8 | - | - |
| `slug_name` | Nullable(String) | 100.0% | 1,858 | - | - |
| `url` | Nullable(String) | 100.0% | 2,394 | - | - |
| `image_url` | Nullable(String) | 0.0% | 0 | - | - |
| `overview` | Nullable(String) | 100.0% | 2,380 | - | - |
| `conditions_of_sale` | Nullable(String) | 100.0% | 1,390 | - | - |
| `sale_total` | Nullable(Float64) | 0.0% | 0 | - | - |
| `lot_count` | Nullable(Int32) | 0.0% | 0 | - | - |
| `scraped_at` | DateTime | 100.0% | 138 | 2026-01-26 02:58:57 | 2026-01-26 03:01:19 |
| `created_at` | DateTime | 100.0% | 2,394 | 2026-01-15 14:52:27 | 2026-01-16 01:12:10 |
| `updated_at` | DateTime | 100.0% | 2,394 | 2026-01-15 15:06:00 | 2026-01-16 01:12:10 |

---

## Table: `sothebys.bronze_lot_pages`

**Row Count:** 99,745

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 85,615 | - | - |
| `auction_uuid` | String | 100.0% | 2,382 | - | - |
| `url` | String | 100.0% | 85,354 | - | - |
| `raw_html` | String | 100.0% | 1 | - | - |
| `content_hash` | String | 100.0% | 85,645 | - | - |
| `http_status` | Int32 | 100.0% | 1 | 200 | 200 |
| `scraped_at` | DateTime | 100.0% | 40,950 | 2026-01-21 12:59:08 | 2026-01-25 07:39:43 |
| `page_size_bytes` | Int64 | 100.0% | 75,424 | 252118 | 1731886 |

---

## Table: `sothebys.fx_rates`

**Row Count:** 16,854

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `rate_date` | Date | 100.0% | 2,809 | 2018-05-02 | 2026-01-08 |
| `currency` | String | 100.0% | 6 | - | - |
| `rate_to_usd` | Float64 | 100.0% | 8,065 | 0.12738691226863352 | 1.421201483734349 |
| `fetched_at` | DateTime | 100.0% | 1 | 2026-01-21 17:03:34 | 2026-01-21 17:03:34 |

---

## Table: `sothebys.gold_features`

**Row Count:** 88,620

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 88,909 | - | - |
| `surface_area_cm2` | Nullable(Float64) | 45.9% | 22,943 | 0.6 | 601261.0800000001 |
| `log_hammer_price` | Nullable(Float64) | 33.3% | 12,943 | -0.02644717001484828 | 16.860032995687696 |
| `log_surface_area` | Nullable(Float64) | 45.9% | 22,742 | -0.5108256237659907 | 13.306784528506737 |
| `artist_id` | Nullable(Int64) | 66.2% | 2,103 | 99999 | 102101 |
| `is_rare_artist` | UInt8 | 100.0% | 2 | 0 | 1 |
| `vital_status` | Nullable(String) | 100.0% | 3 | - | - |
| `computed_at` | DateTime | 100.0% | 1 | 2026-01-25 20:29:47 | 2026-01-25 20:29:47 |

---

## Table: `sothebys.lots`

**Row Count:** 99,971

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 100,423 | - | - |
| `auction_uuid` | String | 100.0% | 2,394 | - | - |
| `lot_number` | Nullable(Int32) | 100.0% | 3,651 | 1 | 9901 |
| `title` | Nullable(String) | 100.0% | 87,262 | - | - |
| `subtitle` | Nullable(String) | 2.3% | 1,836 | - | - |
| `creator` | Nullable(String) | 39.1% | 11,901 | - | - |
| `slug` | Nullable(String) | 100.0% | 88,790 | - | - |
| `estimate_low` | Nullable(Float64) | 99.4% | 297 | 10 | 255000000 |
| `estimate_high` | Nullable(Float64) | 99.4% | 332 | 20 | 350000000 |
| `tags` | Nullable(String) | 100.0% | 2 | - | - |
| `accepts_crypto` | UInt8 | 100.0% | 2 | 0 | 1 |
| `withdrawn_state` | Nullable(String) | 100.0% | 2 | - | - |
| `session_id` | Nullable(Int32) | 100.0% | 2 | 0 | 1 |
| `created_at` | DateTime | 100.0% | 2,448 | 2026-01-15 14:52:27 | 2026-01-16 01:12:10 |
| `updated_at` | DateTime | 100.0% | 2,448 | 2026-01-15 15:06:00 | 2026-01-16 01:12:10 |

---

## Table: `sothebys.raw_auctions`

**Row Count:** 2,390

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_uuid` | String | 100.0% | 2,390 | - | - |
| `sap_sale_number` | Nullable(String) | 100.0% | 2,390 | - | - |
| `date_starts_closing` | Nullable(String) | 0.0% | 0 | - | - |
| `currency` | Nullable(String) | 100.0% | 7 | - | - |
| `lot_count` | Nullable(Int32) | 100.0% | 48 | 1 | 48 |

---

## Table: `sothebys.raw_lots`

**Row Count:** 99,742

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 81,837 | - | - |
| `auction_uuid` | Nullable(String) | 100.0% | 2,380 | - | - |
| `lot_number` | Nullable(String) | 7.0% | 1,151 | - | - |
| `sap_sale_number` | Nullable(String) | 100.0% | 2,380 | - | - |
| `slug` | Nullable(String) | 100.0% | 73,353 | - | - |
| `title` | Nullable(String) | 100.0% | 72,148 | - | - |
| `subtitle` | Nullable(String) | 2.3% | 1,506 | - | - |
| `description_html` | Nullable(String) | 100.0% | 1 | - | - |
| `description_text` | Nullable(String) | 100.0% | 80,259 | - | - |
| `creators_display` | Nullable(String) | 39.2% | 10,434 | - | - |
| `designation_line` | Nullable(String) | 37.3% | 4,727 | - | - |
| `object_type` | Nullable(String) | 100.0% | 52 | - | - |
| `estimate_low` | Nullable(Float64) | 99.4% | 278 | 20 | 175000000 |
| `estimate_high` | Nullable(Float64) | 99.4% | 312 | 30 | 235000000 |
| `currency` | Nullable(String) | 100.0% | 7 | - | - |
| `provenance` | Nullable(String) | 100.0% | 33,687 | - | - |
| `literature` | Nullable(String) | 100.0% | 15,640 | - | - |
| `exhibition` | Nullable(String) | 100.0% | 11,152 | - | - |
| `catalogue_note` | Nullable(String) | 100.0% | 17,110 | - | - |
| `saleroom_notice` | Nullable(String) | 100.0% | 1,806 | - | - |
| `session_date` | Nullable(String) | 100.0% | 2,224 | - | - |
| `symbols_json` | Nullable(String) | 40.9% | 517 | - | - |
| `images_json` | Nullable(String) | 100.0% | 81,459 | - | - |
| `prev_lot_uuid` | Nullable(String) | 97.6% | 80,003 | - | - |
| `next_lot_uuid` | Nullable(String) | 99.4% | 81,364 | - | - |
| `raw_json` | Nullable(String) | 100.0% | 1 | - | - |
| `extracted_at` | Nullable(String) | 0.0% | 0 | - | - |

---

## Table: `sothebys.review_decisions`

**Row Count:** 12

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | Int64 | 100.0% | 12 | 1 | 18 |
| `lot_uuid` | String | 100.0% | 3 | - | - |
| `field_name` | String | 100.0% | 5 | - | - |
| `decision` | String | 100.0% | 3 | - | - |
| `original_value` | Nullable(String) | 8.3% | 1 | - | - |
| `corrected_value` | Nullable(String) | 8.3% | 1 | - | - |
| `original_confidence` | Nullable(Float64) | 100.0% | 2 | 0 | 1 |
| `reviewed_at` | DateTime | 100.0% | 3 | 2026-01-21 13:54:59 | 2026-01-21 14:14:46 |

---

## Table: `sothebys.review_queue`

**Row Count:** 3

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 3 | - | - |
| `queue_position` | Int32 | 100.0% | 3 | 0 | 2 |
| `reason` | String | 100.0% | 1 | - | - |
| `added_at` | DateTime | 100.0% | 1 | 2026-01-21 14:30:56 | 2026-01-21 14:30:56 |

---

## Table: `sothebys.sales`

**Row Count:** 99,971

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 79,484 | - | - |
| `is_closed` | UInt8 | 100.0% | 1 | 1 | 1 |
| `reserve_met` | Nullable(UInt8) | 100.0% | 2 | 0 | 1 |
| `num_bids` | Nullable(Int32) | 39.9% | 86 | 1 | 107 |
| `starting_bid` | Nullable(Float64) | 100.0% | 327 | 1 | 200000000 |
| `hammer_price` | Nullable(Float64) | 39.9% | 208 | 1 | 21000000 |
| `final_price` | Nullable(Float64) | 39.9% | 725 | 1 | 24393000 |
| `currency` | Nullable(String) | 39.9% | 7 | - | - |
| `is_sold` | UInt8 | 100.0% | 2 | 0 | 1 |
| `bid_method` | Nullable(String) | 100.0% | 4 | - | - |
| `closing_time` | Nullable(DateTime) | 15.6% | 12,317 | 2018-05-24 17:11:57 | 2026-01-08 14:20:49 |
| `created_at` | DateTime | 100.0% | 1,910 | 2026-01-15 14:52:27 | 2026-01-15 22:42:12 |
| `updated_at` | DateTime | 100.0% | 1,910 | 2026-01-15 15:06:00 | 2026-01-15 22:42:12 |

---

## Table: `sothebys.silver_extractions`

**Row Count:** 88,620

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 88,909 | - | - |
| `auction_uuid` | String | 100.0% | 2,386 | - | - |
| `extracted_at` | DateTime | 100.0% | 16,635 | 2026-01-21 18:10:29 | 2026-01-25 19:02:17 |
| `extraction_version` | String | 100.0% | 1 | - | - |
| `artist_name` | Nullable(String) | 66.2% | 17,768 | - | - |
| `artist_nationality` | Nullable(String) | 15.7% | 320 | - | - |
| `artist_birth_year` | Nullable(Int32) | 45.9% | 632 | 1000 | 2015 |
| `artist_death_year` | Nullable(Int32) | 32.9% | 622 | 1000 | 2100 |
| `artist_name_confidence` | Float64 | 100.0% | 10 | 0 | 1 |
| `artist_nationality_confidence` | Float64 | 100.0% | 5 | 0 | 1 |
| `artist_dates_confidence` | Float64 | 100.0% | 8 | 0 | 1 |
| `height_cm` | Nullable(Float64) | 52.6% | 2,222 | 0.6 | 1000 |
| `width_cm` | Nullable(Float64) | 46.0% | 2,259 | 0.3 | 1000 |
| `depth_cm` | Nullable(Float64) | 5.6% | 717 | 0.3 | 938.1 |
| `dimensions_confidence` | Float64 | 100.0% | 2 | 0 | 1 |
| `medium` | Nullable(String) | 88.1% | 12,198 | - | - |
| `support` | Nullable(String) | 58.8% | 3,747 | - | - |
| `medium_confidence` | Float64 | 100.0% | 6 | 0 | 1 |
| `creation_year` | Nullable(Int32) | 77.6% | 802 | 1000 | 2100 |
| `creation_is_approximate` | UInt8 | 100.0% | 2 | 0 | 1 |
| `creation_period` | Nullable(String) | 14.1% | 2,057 | - | - |
| `creation_confidence` | Float64 | 100.0% | 6 | 0 | 1 |
| `creation_source` | String | 100.0% | 2 | - | - |
| `tax_bonded` | UInt8 | 100.0% | 1 | 0 | 0 |
| `tax_vat` | UInt8 | 100.0% | 1 | 0 | 0 |
| `is_guaranteed` | UInt8 | 100.0% | 1 | 0 | 0 |
| `regime_1031` | UInt8 | 100.0% | 1 | 0 | 0 |
| `hammer_price_usd` | Nullable(Float64) | 33.3% | 12,954 | 0.9738994935722634 | 21000000 |
| `price_normalized_at` | Nullable(DateTime) | 100.0% | 7 | 2026-01-25 20:12:07 | 2026-01-25 20:29:39 |
| `enriched_at` | Nullable(DateTime) | 100.0% | 1,335 | 2026-01-25 20:06:11 | 2026-01-25 20:28:43 |
| `raw_description` | Nullable(String) | 100.0% | 87,370 | - | - |
| `extraction_error` | Nullable(String) | 0.0% | 0 | - | - |

---

## Table: `sothebys.v_gold_with_artist`

**Row Count:** 88,620

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 88,909 | - | - |
| `surface_area_cm2` | Nullable(Float64) | 45.9% | 22,943 | 0.6 | 601261.0800000001 |
| `log_hammer_price` | Nullable(Float64) | 33.3% | 12,943 | -0.02644717001484828 | 16.860032995687696 |
| `log_surface_area` | Nullable(Float64) | 45.9% | 22,742 | -0.5108256237659907 | 13.306784528506737 |
| `artist_id` | Nullable(Int64) | 66.2% | 2,103 | 99999 | 102101 |
| `is_rare_artist` | UInt8 | 100.0% | 2 | 0 | 1 |
| `vital_status` | Nullable(String) | 100.0% | 3 | - | - |
| `computed_at` | DateTime | 100.0% | 1 | 2026-01-25 20:29:47 | 2026-01-25 20:29:47 |
| `artist_name` | String | 100.0% | 2,104 | - | - |
| `artist_lot_count` | Int32 | 100.0% | 117 | 0 | 1648 |

---

## Table: `sothebys.v_lot_with_sales`

**Row Count:** 120,942

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `l.lot_uuid` | String | 100.0% | 100,423 | - | - |
| `l.auction_uuid` | String | 100.0% | 2,394 | - | - |
| `lot_number` | Nullable(Int32) | 100.0% | 3,651 | 1 | 9901 |
| `l.title` | Nullable(String) | 100.0% | 87,262 | - | - |
| `creator` | Nullable(String) | 39.9% | 11,901 | - | - |
| `estimate_low` | Nullable(Float64) | 99.3% | 297 | 10 | 255000000 |
| `estimate_high` | Nullable(Float64) | 99.3% | 332 | 20 | 350000000 |
| `hammer_price` | Nullable(Float64) | 33.0% | 208 | 1 | 21000000 |
| `final_price` | Nullable(Float64) | 33.0% | 725 | 1 | 24393000 |
| `is_sold` | UInt8 | 100.0% | 2 | 0 | 1 |
| `num_bids` | Nullable(Int32) | 33.0% | 86 | 1 | 107 |
| `auction_title` | String | 100.0% | 1,626 | - | - |
| `department` | Nullable(String) | 99.9% | 95 | - | - |
| `location` | Nullable(String) | 99.9% | 13 | - | - |
| `date_starts_closing` | Nullable(DateTime) | 0.6% | 12 | 2018-05-24 17:00:57 | 2025-12-04 12:00:59 |

---

## Table: `sothebys.v_silver_with_auction`

**Row Count:** 88,620

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 88,909 | - | - |
| `auction_uuid` | String | 100.0% | 2,386 | - | - |
| `extracted_at` | DateTime | 100.0% | 16,635 | 2026-01-21 18:10:29 | 2026-01-25 19:02:17 |
| `extraction_version` | String | 100.0% | 1 | - | - |
| `artist_name` | Nullable(String) | 66.2% | 17,768 | - | - |
| `artist_nationality` | Nullable(String) | 15.7% | 320 | - | - |
| `artist_birth_year` | Nullable(Int32) | 45.9% | 632 | 1000 | 2015 |
| `artist_death_year` | Nullable(Int32) | 32.9% | 622 | 1000 | 2100 |
| `artist_name_confidence` | Float64 | 100.0% | 10 | 0 | 1 |
| `artist_nationality_confidence` | Float64 | 100.0% | 5 | 0 | 1 |
| `artist_dates_confidence` | Float64 | 100.0% | 8 | 0 | 1 |
| `height_cm` | Nullable(Float64) | 52.6% | 2,222 | 0.6 | 1000 |
| `width_cm` | Nullable(Float64) | 46.0% | 2,259 | 0.3 | 1000 |
| `depth_cm` | Nullable(Float64) | 5.6% | 717 | 0.3 | 938.1 |
| `dimensions_confidence` | Float64 | 100.0% | 2 | 0 | 1 |
| `medium` | Nullable(String) | 88.1% | 12,198 | - | - |
| `support` | Nullable(String) | 58.8% | 3,747 | - | - |
| `medium_confidence` | Float64 | 100.0% | 6 | 0 | 1 |
| `creation_year` | Nullable(Int32) | 77.6% | 802 | 1000 | 2100 |
| `creation_is_approximate` | UInt8 | 100.0% | 2 | 0 | 1 |
| `creation_period` | Nullable(String) | 14.1% | 2,057 | - | - |
| `creation_confidence` | Float64 | 100.0% | 6 | 0 | 1 |
| `creation_source` | String | 100.0% | 2 | - | - |
| `tax_bonded` | UInt8 | 100.0% | 1 | 0 | 0 |
| `tax_vat` | UInt8 | 100.0% | 1 | 0 | 0 |
| `is_guaranteed` | UInt8 | 100.0% | 1 | 0 | 0 |
| `regime_1031` | UInt8 | 100.0% | 1 | 0 | 0 |
| `hammer_price_usd` | Nullable(Float64) | 33.3% | 12,954 | 0.9738994935722634 | 21000000 |
| `price_normalized_at` | Nullable(DateTime) | 100.0% | 7 | 2026-01-25 20:12:07 | 2026-01-25 20:29:39 |
| `enriched_at` | Nullable(DateTime) | 100.0% | 1,335 | 2026-01-25 20:06:11 | 2026-01-25 20:28:43 |
| `raw_description` | Nullable(String) | 100.0% | 87,370 | - | - |
| `extraction_error` | Nullable(String) | 0.0% | 0 | - | - |
| `auction_title` | String | 100.0% | 1,618 | - | - |
| `department` | Nullable(String) | 99.9% | 94 | - | - |
| `location` | Nullable(String) | 99.9% | 12 | - | - |
| `date_starts_closing` | Nullable(DateTime) | 0.6% | 12 | 2018-05-24 17:00:57 | 2025-12-04 12:00:59 |

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

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_uuid` | String | 100.0% | 1 | - | - |
| `title` | String | 100.0% | 1 | - | - |
| `sap_sale_number` | Nullable(String) | 0.0% | 0 | - | - |
| `department` | Nullable(String) | 0.0% | 0 | - | - |
| `category` | Nullable(String) | 0.0% | 0 | - | - |
| `currency` | Nullable(String) | 0.0% | 0 | - | - |
| `auction_type` | Nullable(String) | 0.0% | 0 | - | - |
| `state` | Nullable(String) | 0.0% | 0 | - | - |
| `location` | Nullable(String) | 0.0% | 0 | - | - |
| `timezone` | Nullable(String) | 0.0% | 0 | - | - |
| `date_opens` | Nullable(DateTime) | 0.0% | 0 | - | - |
| `date_starts_closing` | Nullable(DateTime) | 0.0% | 0 | - | - |
| `date_closed` | Nullable(DateTime) | 0.0% | 0 | - | - |
| `date_published` | Nullable(DateTime) | 0.0% | 0 | - | - |
| `date_range` | Nullable(String) | 0.0% | 0 | - | - |
| `time` | Nullable(String) | 0.0% | 0 | - | - |
| `slug_year` | Nullable(String) | 0.0% | 0 | - | - |
| `slug_name` | Nullable(String) | 0.0% | 0 | - | - |
| `url` | Nullable(String) | 100.0% | 1 | - | - |
| `image_url` | Nullable(String) | 0.0% | 0 | - | - |
| `overview` | Nullable(String) | 0.0% | 0 | - | - |
| `conditions_of_sale` | Nullable(String) | 0.0% | 0 | - | - |
| `sale_total` | Nullable(Float64) | 0.0% | 0 | - | - |
| `lot_count` | Nullable(Int32) | 0.0% | 0 | - | - |
| `scraped_at` | DateTime | 100.0% | 1 | 2026-01-28 05:18:49 | 2026-01-28 05:18:49 |
| `created_at` | DateTime | 100.0% | 1 | 2026-01-28 05:18:49 | 2026-01-28 05:18:49 |
| `updated_at` | DateTime | 100.0% | 1 | 2026-01-28 05:18:49 | 2026-01-28 05:18:49 |

---

## Table: `auction_19th_century_american_and_western_art.lot_images`

**Row Count:** 517

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_id` | String | 100.0% | 1 | - | - |
| `lot_id` | String | 100.0% | 110 | - | - |
| `image_url` | String | 100.0% | 408 | - | - |
| `position` | UInt16 | 100.0% | 5 | 1 | 5 |
| `fetched_at` | DateTime | 100.0% | 52 | 2026-01-28 04:18:49 | 2026-01-28 04:19:40 |

---

## Table: `auction_19th_century_american_and_western_art.lots`

**Row Count:** 110

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 110 | - | - |
| `auction_uuid` | String | 100.0% | 1 | - | - |
| `lot_number` | Nullable(Int32) | 100.0% | 110 | 401 | 511 |
| `title` | Nullable(String) | 100.0% | 109 | - | - |
| `subtitle` | Nullable(String) | 0.0% | 0 | - | - |
| `creator` | Nullable(String) | 100.0% | 109 | - | - |
| `slug` | Nullable(String) | 0.0% | 0 | - | - |
| `estimate_low` | Nullable(Float64) | 0.9% | 1 | 12126362000 | 12126362000 |
| `estimate_high` | Nullable(Float64) | 0.0% | 0 | - | - |
| `tags` | Nullable(String) | 0.0% | 0 | - | - |
| `accepts_crypto` | UInt8 | 100.0% | 1 | 0 | 0 |
| `withdrawn_state` | Nullable(String) | 35.5% | 1 | - | - |
| `session_id` | Nullable(Int32) | 0.0% | 0 | - | - |
| `created_at` | DateTime | 100.0% | 1 | 2026-01-28 05:19:42 | 2026-01-28 05:19:42 |
| `updated_at` | DateTime | 100.0% | 1 | 2026-01-28 05:19:42 | 2026-01-28 05:19:42 |

---

## Table: `auction_19th_century_american_and_western_art.pages_raw`

**Row Count:** 121

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_id` | String | 100.0% | 1 | - | - |
| `lot_id` | Nullable(String) | 90.9% | 110 | - | - |
| `url` | String | 100.0% | 121 | - | - |
| `final_url` | String | 100.0% | 121 | - | - |
| `page_type` | LowCardinality(String) | 100.0% | 2 | - | - |
| `http_status` | UInt16 | 100.0% | 1 | 200 | 200 |
| `fetched_at` | DateTime | 100.0% | 55 | 2026-01-28 04:18:49 | 2026-01-28 04:24:52 |
| `html` | String | 100.0% | 121 | - | - |
| `html_sha256` | FixedString(64) | 100.0% | 121 | - | - |
| `parse_version` | LowCardinality(String) | 100.0% | 1 | - | - |

---

# Database: `collector_connoisseur_the_max_n_berry_collections_american_art_d`

## Table: `collector_connoisseur_the_max_n_berry_collections_american_art_d.auctions`

**Row Count:** 1

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_uuid` | String | 100.0% | 1 | - | - |
| `title` | String | 100.0% | 1 | - | - |
| `sap_sale_number` | Nullable(String) | 0.0% | 0 | - | - |
| `department` | Nullable(String) | 0.0% | 0 | - | - |
| `category` | Nullable(String) | 0.0% | 0 | - | - |
| `currency` | Nullable(String) | 0.0% | 0 | - | - |
| `auction_type` | Nullable(String) | 0.0% | 0 | - | - |
| `state` | Nullable(String) | 0.0% | 0 | - | - |
| `location` | Nullable(String) | 0.0% | 0 | - | - |
| `timezone` | Nullable(String) | 0.0% | 0 | - | - |
| `date_opens` | Nullable(DateTime) | 0.0% | 0 | - | - |
| `date_starts_closing` | Nullable(DateTime) | 0.0% | 0 | - | - |
| `date_closed` | Nullable(DateTime) | 0.0% | 0 | - | - |
| `date_published` | Nullable(DateTime) | 0.0% | 0 | - | - |
| `date_range` | Nullable(String) | 0.0% | 0 | - | - |
| `time` | Nullable(String) | 0.0% | 0 | - | - |
| `slug_year` | Nullable(String) | 0.0% | 0 | - | - |
| `slug_name` | Nullable(String) | 0.0% | 0 | - | - |
| `url` | Nullable(String) | 100.0% | 1 | - | - |
| `image_url` | Nullable(String) | 0.0% | 0 | - | - |
| `overview` | Nullable(String) | 0.0% | 0 | - | - |
| `conditions_of_sale` | Nullable(String) | 0.0% | 0 | - | - |
| `sale_total` | Nullable(Float64) | 0.0% | 0 | - | - |
| `lot_count` | Nullable(Int32) | 0.0% | 0 | - | - |
| `scraped_at` | DateTime | 100.0% | 1 | 2026-01-28 05:19:43 | 2026-01-28 05:19:43 |
| `created_at` | DateTime | 100.0% | 1 | 2026-01-28 05:19:43 | 2026-01-28 05:19:43 |
| `updated_at` | DateTime | 100.0% | 1 | 2026-01-28 05:19:43 | 2026-01-28 05:19:43 |

---

## Table: `collector_connoisseur_the_max_n_berry_collections_american_art_d.lot_images`

**Row Count:** 351

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_id` | String | 100.0% | 1 | - | - |
| `lot_id` | String | 100.0% | 75 | - | - |
| `image_url` | String | 100.0% | 277 | - | - |
| `position` | UInt16 | 100.0% | 5 | 1 | 5 |
| `fetched_at` | DateTime | 100.0% | 33 | 2026-01-28 04:19:44 | 2026-01-28 04:20:16 |

---

## Table: `collector_connoisseur_the_max_n_berry_collections_american_art_d.lots`

**Row Count:** 75

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `lot_uuid` | String | 100.0% | 75 | - | - |
| `auction_uuid` | String | 100.0% | 1 | - | - |
| `lot_number` | Nullable(Int32) | 100.0% | 75 | 301 | 375 |
| `title` | Nullable(String) | 100.0% | 75 | - | - |
| `subtitle` | Nullable(String) | 0.0% | 0 | - | - |
| `creator` | Nullable(String) | 100.0% | 75 | - | - |
| `slug` | Nullable(String) | 0.0% | 0 | - | - |
| `estimate_low` | Nullable(Float64) | 0.0% | 0 | - | - |
| `estimate_high` | Nullable(Float64) | 0.0% | 0 | - | - |
| `tags` | Nullable(String) | 0.0% | 0 | - | - |
| `accepts_crypto` | UInt8 | 100.0% | 1 | 0 | 0 |
| `withdrawn_state` | Nullable(String) | 40.0% | 1 | - | - |
| `session_id` | Nullable(Int32) | 0.0% | 0 | - | - |
| `created_at` | DateTime | 100.0% | 1 | 2026-01-28 05:20:18 | 2026-01-28 05:20:18 |
| `updated_at` | DateTime | 100.0% | 1 | 2026-01-28 05:20:18 | 2026-01-28 05:20:18 |

---

## Table: `collector_connoisseur_the_max_n_berry_collections_american_art_d.pages_raw`

**Row Count:** 86

| Column | Type | Fill Rate | Unique Vals | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `auction_id` | String | 100.0% | 1 | - | - |
| `lot_id` | Nullable(String) | 87.2% | 75 | - | - |
| `url` | String | 100.0% | 86 | - | - |
| `final_url` | String | 100.0% | 86 | - | - |
| `page_type` | LowCardinality(String) | 100.0% | 2 | - | - |
| `http_status` | UInt16 | 100.0% | 1 | 200 | 200 |
| `fetched_at` | DateTime | 100.0% | 35 | 2026-01-28 04:19:44 | 2026-01-28 04:25:54 |
| `html` | String | 100.0% | 86 | - | - |
| `html_sha256` | FixedString(64) | 100.0% | 86 | - | - |
| `parse_version` | LowCardinality(String) | 100.0% | 1 | - | - |

---

