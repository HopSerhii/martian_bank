


import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  current_transfer: [],
  isLoading: false,
  error: null,
};

const transferSlice = createSlice({
  name: "transfer",
  initialState,
  reducers: {
    createTransfer: (state, action) => {
      state.current_transfer = action.payload;
    },
  },
});

export const { createTransfer } = transferSlice.actions;

export default transferSlice.reducer;
