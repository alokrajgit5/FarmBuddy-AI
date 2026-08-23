import api from "./axios";

// Hire Labor
export const hireLabor = async (data) => {
  const response = await api.post(
    "/api/labor-bookings/",
    data
  );

  return response.data;
};

// My Hired Labors
export const getMyLaborBookings = async () => {
  const response = await api.get(
    "/api/labor-bookings/my-bookings"
  );

  return response.data;
};

// Booking Details
export const getLaborBookingById = async (id) => {
  const response = await api.get(
    `/api/labor-bookings/${id}`
  );

  return response.data;
};

// Cancel Booking
export const cancelLaborBooking = async (id) => {
  const response = await api.delete(
    `/api/labor-bookings/${id}`
  );

  return response.data;
};