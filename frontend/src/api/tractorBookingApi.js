import api from "./axios";

// Create Booking
export const createBooking = async (bookingData) => {

  const response = await api.post(
    "/api/tractor-bookings/",
    bookingData
  );

  return response.data;

};

// My Bookings
export const getMyBookings = async () => {

  const response = await api.get(
    "/api/tractor-bookings/my-bookings"
  );

  return response.data;

};

// Booking Details
export const getBookingById = async (id) => {

  const response = await api.get(
    `/api/tractor-bookings/${id}`
  );

  return response.data;

};

// Cancel Booking
export const cancelBooking = async (id) => {

  const response = await api.delete(
    `/api/tractor-bookings/${id}`
  );

  return response.data;

};