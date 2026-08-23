import api from "./axios";

// Buy Seed
export const buySeed = async (data) => {

  const response = await api.post(
    "/api/seed-purchases/",
    data
  );

  return response.data;

};

// My Seed Purchases
export const getMySeedPurchases = async () => {

  const response = await api.get(
    "/api/seed-purchases/my-purchases"
  );

  return response.data;

};

// Get Purchase By ID
export const getSeedPurchaseById = async (id) => {

  const response = await api.get(
    `/api/seed-purchases/${id}`
  );

  return response.data;

};

// Delete Purchase
export const deleteSeedPurchase = async (id) => {

  const response = await api.delete(
    `/api/seed-purchases/${id}`
  );

  return response.data;

};