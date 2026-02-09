import { useState } from "react";
import { useSubmitPromptMutation } from "./services/api";
import PromptForm from "./features/prompt/PromptForm";
import InsightsList from "./features/prompt/InsightsList";

function App() {
  const [submitPrompt, mutationState] = useSubmitPromptMutation();
  const [lastRequest, setLastRequest] = useState(null);

  const handleSubmit = async (formData) => {
    setLastRequest(formData);
    await submitPrompt(formData);
  };

  return (
    <div className="container">
      <h1>AI Insights Client</h1>
      <PromptForm onSubmit={handleSubmit} />
      <InsightsList
        lastRequest={lastRequest}
        mutationState={mutationState}
        submitPrompt={submitPrompt}
      />
    </div>
  );
}

export default App;
