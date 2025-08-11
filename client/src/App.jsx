import {
    Box,
    CssBaseline,
    ThemeProvider,
    createTheme,
} from "@mui/material"

import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom"

import { SnackbarProvider } from "./components/SnackbarContext"

import "./App.css"

const theme = createTheme({

})

const SamplePage = () => {
    return (
        <Box>Hello World!</Box>
    )
}

const routes = [
    {
        path: "/",
        element: <SamplePage />
    }
]

function App() {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Router>
                <SnackbarProvider>
                    <Routes>
                        {routes.map((item) => (
                            <Route path={item.path} element={item.element} />
                        ))}
                    </Routes>
                </SnackbarProvider>
            </Router>
        </ThemeProvider>
    )
}

export default App
