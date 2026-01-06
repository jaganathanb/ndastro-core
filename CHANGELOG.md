# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-01-06

### Added
- New `get_planet_position` function in core module for calculating planetary positions
- Support for ayanamsa parameter in planetary position calculations for sidereal astronomy
- Four new enum modules:
  - `planet_enum.py`: Planets enumeration with color codes and planet codes
  - `house_enum.py`: Houses enumeration with owner planet properties
  - `nakshatra_enum.py`: Natchaththirams (Nakshatras/Stars) enumeration
  - `rasi_enum.py`: Rasis (Zodiac signs) enumeration with 4x4 grid representation
- Comprehensive test suite for `get_planet_position` function with multiple test cases
- Support for ecliptic coordinate frame calculations

### Changed
- Reorganized test files structure
- Enhanced type hints with TYPE_CHECKING guards for better performance

## [0.2.1] - 2026-01-06

### Changed
- Updated `get_sunrise_sunset` function signature to use `float` parameters for latitude and longitude instead of `skyfield.units.Angle` objects
- Updated README.md documentation with simplified API examples using float coordinates

### Fixed
- Improved API usability by removing the need for Angle object imports

## [0.2.0] - 2026-01-05

### Added
- Initial public release on PyPI
- Sunrise and sunset calculation functionality
- Support for WGS84 coordinates
- Automatic JPL ephemeris data management (DE441)
- Type hints throughout the codebase
- Comprehensive test suite
- Configuration management for ephemeris data

### Documentation
- Complete README with usage examples
- API documentation
- Installation instructions

## [Unreleased]

### Planned
- Additional astronomical calculations (moon phases, planetary positions)
- Support for more astronomical events
- Performance optimizations
- Extended documentation and examples

---

[0.3.0]: https://github.com/jaganathanb/ndastro-core/releases/tag/v0.3.0
[0.2.1]: https://github.com/jaganathanb/ndastro-core/releases/tag/v0.2.1
[0.2.0]: https://github.com/jaganathanb/ndastro-core/releases/tag/v0.2.0
