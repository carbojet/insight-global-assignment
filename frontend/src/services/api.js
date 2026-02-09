import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const api = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({
    baseUrl: import.meta.env.VITE_API_BASE_URL,
  }),
  endpoints: (builder) => ({
    submitPrompt: builder.mutation({
      query: ({ prompt, targetLanguage, page = 1, pageSize = 10 }) => ({
        url: `/prompts?page=${page}&pageSize=${pageSize}`,
        method: "POST",
        body: { prompt, targetLanguage },
      }),
    }),
  }),
});

export const { useSubmitPromptMutation } = api;
