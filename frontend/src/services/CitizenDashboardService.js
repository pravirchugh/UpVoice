import ApiService from "./ApiService";

const ENDPOINTS = {
  FETCH_COMPANIES: "common/fetch-company-list",
  FETCH_COMPANIES_CATEGORIES: "common/fetch-company-categories",
};

class CitizenDashboardService extends ApiService {
  constructor() {
    super();
  }

  fetchCompanies = async () => {
    const { data } = await this.apiClient.post(ENDPOINTS.FETCH_COMPANIES);
    return data;
  };

  fetchCompanyCategories = async () => {
    const { data } = await this.apiClient.post(ENDPOINTS.FETCH_COMPANIES_CATEGORIES);
    return data;
  };
}

const citizenDashboardService = new CitizenDashboardService();

export default citizenDashboardService;
