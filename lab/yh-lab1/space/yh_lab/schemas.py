from pydantic import BaseModel, Field


class EvalSummary(BaseModel):
    lab_id: str = 'YH-LAB1'
    product_release: str = 'YH-MANAGED-0.1.0'
    blueprint: str = 'BP-SLEEP-001@1.0.0'
    fixture_counts: dict[str, int]
    routes: list[str]
    run_status: str


class RouteResult(BaseModel):
    route_id: str
    case_id: str
    status: str
    conclusion: str | None = None


class AdmissionStatus(BaseModel):
    verdict: str = Field(pattern='^(ADMIT|HOLD|FAIL)$')
    reason: str
