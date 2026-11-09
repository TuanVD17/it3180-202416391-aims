# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-11-09
### Fixed
- Make search_by_title case-insensitive (Refs #18).

## [1.0.0] - 2026-11-09
### Added
- Cart.print_cart(): print formatted cart contents and total cost.
- search_by_title(): search DVDs in cart/store by title.
- total_cost_with_discount(): support percentage discount.

### Fixed
- Cart accepts the 21st DVD although the limit is 20 (Off-by-one bug).
