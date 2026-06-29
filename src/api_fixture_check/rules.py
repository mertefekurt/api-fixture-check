from __future__ import annotations

from api_fixture_check.models import Rule

PROJECT_NAME = 'api-fixture-check'
DESCRIPTION = 'Audit API test fixtures for realism, identifiers, and brittle values.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = 'fixture user id 123 email test@test.com only happy path no negative case'
MEDIUM_SAMPLE = '\\b(happy path only|no negative case|success only)\\b'
CLEAN_SAMPLE = 'fixture user id usr_9f2 email user@example.test includes invalid_token case'

RULES = (
    Rule(
        code='placeholder-identity',
        severity='high',
        pattern='\\b(test@test\\.com|foo@bar|john doe|id\\s*[:=]\\s*123)\\b',
        message='placeholder identity detected',
        recommendation='Use realistic non-production fixture values.',
    ),
    Rule(
        code='happy-path-only',
        severity='medium',
        pattern='\\b(happy path only|no negative case|success only)\\b',
        message='fixture set lacks negative cases',
        recommendation='Add failure, boundary, and permission-denied cases.',
    ),
    Rule(
        code='brittle-timestamp',
        severity='low',
        pattern='\\b(2020-01-01|1970-01-01|now\\(\\))\\b',
        message='timestamp fixture may be brittle',
        recommendation='Use stable generated timestamps or explicit test clocks.',
    ),
)
