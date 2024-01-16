


import { apiSlice } from "./usersApiSlice";
import ApiUrls from "./apiUrls";

const atmUrl = import.meta.env.VITE_ATM_URL || ApiUrls.VITE_ATM_URL;

export const atmApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    getAtms: builder.mutation({
      query: (data) => ({
        url: `${atmUrl}`,
        method: "POST",
        body: data,
      }),
    }),
    getParticularATM: builder.mutation({
      query: (id) => ({
        url: `${atmUrl}${id}`,
        method: "GET",
      }),
    }),
  }),
});

export const { useGetAtmsMutation, useGetParticularATMMutation } = atmApiSlice;
