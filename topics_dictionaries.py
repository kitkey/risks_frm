from credit_risk_measurement_and_management import cr_broad_topics, cr_subtopics_dict
from current_issues_in_financial_markets import ci_broad_topics, ci_subtopics_dict
from financial_markets_and_products import fmp_broad_topics, fmp_subtopics_dict
from foundation_of_risks import broad_topics as frm_broad_topics, frm_subtopics
from liquitidy_and_treasury_risk_measurement_and_management import (
    ltr_broad_topics,
    ltr_subtopics_dict,
)
from market_risk_measurement_and_management import mr_broad_topics, mr_subtopics_dict
from operation_risk_and_resilience import orr_broad_topics, orr_subtopics_dict
from quantitive_analysis import qa_broad_topics, qa_subtopics_dict
from risk_management_and_investment_management import im_broad_topics, im_subtopics_dict
from valuation_and_risk_models import vrm_broad_topics, vrm_subtopics_dict


broad = {
    "foundation_of_risks.py": frm_broad_topics,
    "quantitive_analysis.py": qa_broad_topics,
    "financial_markets_and_products.py": fmp_broad_topics,
    "valuation_and_risk_models.py": vrm_broad_topics,
    "market_risk_measurement_and_management.py": mr_broad_topics,
    "credit_risk_measurement_and_management.py": cr_broad_topics,
    "liquitidy_and_treasury_risk_measurement_and_management.py": ltr_broad_topics,
    "operation_risk_and_resilience.py": orr_broad_topics,
    "risk_management_and_investment_management.py": im_broad_topics,
    "current_issues_in_financial_markets.py": ci_broad_topics,
}


standard = {
    "foundation_of_risks.py": frm_subtopics,
    "quantitive_analysis.py": qa_subtopics_dict,
    "financial_markets_and_products.py": fmp_subtopics_dict,
    "valuation_and_risk_models.py": vrm_subtopics_dict,
    "market_risk_measurement_and_management.py": mr_subtopics_dict,
    "credit_risk_measurement_and_management.py": cr_subtopics_dict,
    "liquitidy_and_treasury_risk_measurement_and_management.py": ltr_subtopics_dict,
    "operation_risk_and_resilience.py": orr_subtopics_dict,
    "risk_management_and_investment_management.py": im_subtopics_dict,
    "current_issues_in_financial_markets.py": ci_subtopics_dict,
}
