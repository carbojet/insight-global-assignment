import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";

const schema = z.object({
  prompt: z.string().min(5, "Prompt must be at least 5 characters"),
  targetLanguage: z.string().min(1, "Select a language"),
});

function PromptForm({ onSubmit }) {
  const {
    register,
    handleSubmit,
    formState: { errors, isValid },
  } = useForm({
    resolver: zodResolver(schema),
    mode: "onChange",
  });

  const handleFormSubmit = async (formData) => {
    await onSubmit(formData);
  };

  return (
    <div>
      <h2>Submit Prompt</h2>

      <form onSubmit={handleSubmit(handleFormSubmit)}>
        <div className="form-group">
          <textarea
            placeholder="Enter your prompt..."
            {...register("prompt")}
            rows="4"
            style={{ width: "100%" }}
          />
          {errors.prompt && (
            <p style={{ color: "red" }}>{errors.prompt.message}</p>
          )}
        </div>

        <div className="form-group">
          <select {...register("targetLanguage")} style={{ width: "100%" }}>
            <option value="">Select Language</option>
            <option value="en">English</option>
            <option value="es">Spanish</option>
            <option value="fr">French</option>
          </select>
          {errors.targetLanguage && (
            <p className="error-text">{errors.targetLanguage.message}</p>
          )}
        </div>

        <button
          type="submit"
          disabled={!isValid}
          className="form-group"
        >
          Submit
        </button>
      </form>
    </div>
  );
}

export default PromptForm;
