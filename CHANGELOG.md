# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.1] - 2026-01-06

### Added
- Comprehensive test coverage configuration with pytest-cov and pytest-xdist
- 47 new unit tests covering all core functionality:
  - `test_enums.py`: 17 tests for Planet enum (conversions, properties, operations)
  - `test_core.py`: 18 new tests for planetary calculations and edge cases
  - `test_utils.py`: 11 new tests for normalize_degree function
  - `test_constants.py`: 1 new test for DEGREE_MAX constant
- Test coverage reporting (HTML, XML, terminal)
- Multiple test runner scripts:
  - `run_tests.ps1`: PowerShell script with multiple modes (coverage, unit, integration, fast, parallel)
  - `run_tests.bat`: Batch script for Windows
  - `Makefile`: Cross-platform make targets
- GitHub Actions CI/CD workflow with test matrix (Ubuntu, Windows, macOS × Python 3.10-3.13)
- Test markers system for categorizing tests (unit, integration, slow)
- Comprehensive testing documentation in `TESTING.md`

### Fixed
- **Critical**: Fixed Kethu longitude calculation in `get_all_planet_positions` - was incorrectly using Rahu's latitude instead of longitude, causing Kethu to always be at 180° instead of 180° opposite to Rahu's actual position
- Fixed floating-point precision issues in test assertions

### Changed
- All existing tests now marked with `@pytest.mark.unit` for easy filtering
- Enhanced pytest configuration with coverage options and strict mode
- Updated development dependencies to include pytest-cov>=6.0.0 and pytest-xdist>=3.6.1

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

[0.3.1]: https://github.com/jaganathanb/ndastro-core/releases/tag/v0.3.1
[0.3.0]: https://github.com/jaganathanb/ndastro-core/releases/tag/v0.3.0
[0.2.1]: https://github.com/jaganathanb/ndastro-core/releases/tag/v0.2.1
[0.2.0]: https://github.com/jaganathanb/ndastro-core/releases/tag/v0.2.0
