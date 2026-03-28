export const reportsRoute = {
  path: "/reports",
  method: "GET",
};

export function handleReports() {
  return {
    ok: true,
    route: "reports",
    message: "Starter route for Express Route to FastAPI",
  };
}
