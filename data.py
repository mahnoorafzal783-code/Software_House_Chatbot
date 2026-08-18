# Project data structure

project_data = {
    "project_id": "",
    "client_name": "",
    "company_name": "",
    "service": "",
    "requirements": "",
    "budget": "",
    "timeline": "",
    "estimated_price": "",
    "project_status": ""
}


def create_project_data(
    project_id,
    client_name,
    company_name,
    service,
    requirements,
    budget,
    timeline,
    estimated_price,
    project_status
):
    return {
        "project_id": project_id,
        "client_name": client_name,
        "company_name": company_name,
        "service": service,
        "requirements": requirements,
        "budget": budget,
        "timeline": timeline,
        "estimated_price": estimated_price,
        "project_status": project_status
    }