import ApiService from "./ApiService";

const ENDPOINTS = {
  FETCH_COMPANIES: "common/fetch-company-list",
  FETCH_COMPANIES_CATEGORIES: "common/fetch-company-categories",
  RAISE_A_VOICE: "user/raise-a-voice",
  SEND_AN_EMAIL: "voice/add-voice"
};

class CitizenDashboardService extends ApiService {
  constructor() {
    super();
  }

  fetchCompanies = async () => {
    const { data } = await this.apiClient.get(ENDPOINTS.FETCH_COMPANIES);
    return data;
  };

  fetchCompanyCategories = async () => {
    const { data } = await this.apiClient.get(ENDPOINTS.FETCH_COMPANIES_CATEGORIES);
    return data;
  };

  raiseVoice = async (payload) => {
    const {data} = await this.apiClient.post(ENDPOINTS.RAISE_A_VOICE, payload)
    return data
  }

  sendEmail = async (payload) => {
    const {data} = await this.apiClient.post(ENDPOINTS.SEND_AN_EMAIL, payload)
    return data
  }
}

const citizenDashboardService = new CitizenDashboardService();

export default citizenDashboardService;
