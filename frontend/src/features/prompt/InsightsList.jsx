import { useState, useEffect, useRef } from "react";

function InsightsList({ lastRequest, mutationState, submitPrompt }) {
  const { data, error, isLoading } = mutationState;

  const [page, setPage] = useState(1);
  const [insights, setInsights] = useState([]);
  const loadMoreRef = useRef(null);

  // Reset when new request comes
  useEffect(() => {
    if (lastRequest) {
      setPage(1);
      setInsights([]);
    }
  }, [lastRequest]);

  // Append or replace insights when new data arrives
  useEffect(() => {
    if (data?.status === "SUCCESS") {
      setInsights((prev) =>
        page === 1 ? data.data : [...prev, ...data.data]
      );
    }

    if (page > 1 && loadMoreRef.current) {
      loadMoreRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [data, page]);

  const loadMore = async () => {
    if (!lastRequest) return;

    const nextPage = page + 1;
    setPage(nextPage);

    await submitPrompt({
      ...lastRequest,
      page: nextPage,
    });
  };

  if (!data) return null;

  if (error) {
    return <p className="error-text">Something went wrong.</p>;
  }

  if (data.status === "NEEDS_CLARIFICATION") {
    return <p>{data.message}</p>;
  }

  if (data.status === "SUCCESS") {
    return (
      <div>
        <h3>Insights</h3>

        {insights.map((item) => (
          <div key={item.id} className="card">
            <strong>{item.title}</strong>
            <p>{item.content}</p>
          </div>
        ))}

        {data.pagination.hasNext && (
          <button onClick={loadMore} disabled={isLoading} ref={loadMoreRef}>
            {isLoading ? "Loading..." : "Load More"}

          </button>
        )}
      </div>
    );
  }

  return null;
}

export default InsightsList;
