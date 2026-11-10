return function()
	return {
		file = assert(vim.api.nvim_get_runtime_file("lua/flash-any/tables/tiger.tsv", false)[1]),
		format = "tsv",
		columns = { "text", "code", "weight" },
		matcher = "full_code",
		selection = { keys = { " ", ";" } },
	}
end
