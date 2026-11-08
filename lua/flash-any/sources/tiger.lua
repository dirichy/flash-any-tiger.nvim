return function(opts)
	assert(not opts.scheme, "scheme is only supported by the pinyin source")
	assert(opts.append_space_below == nil, "tiger only supports selection.keys; append_space_below is not supported")
	assert(opts.selection_keys == nil, "use tiger selection.keys")
	assert(
		opts.force == nil and opts.punctuation == nil,
		"tiger selection keys are always optional; remove force/punctuation"
	)
	local config = opts.selection
	if config == nil then
		config = {}
	end
	assert(config == false or type(config) == "table", "tiger selection must be a table or false")
	---@type string[]|false|nil
	local selection = false
	if config then
		assert(config.force == nil and config.first_omit_before == nil, "selection keys are always optional")
		selection = config.keys
		if selection == nil then
			selection = { " ", ";" }
		end
	end
	assert(
		config == false or (type(selection) == "table" and vim.islist(selection) and #selection > 0),
		"tiger selection.keys must be a nonempty list"
	)
	if selection then
		local used = {}
		for index, key in ipairs(selection) do
			assert(
				type(key) == "string"
					and #key == 1
					and key:byte() < 128
					and (key:match("%p") or (index == 1 and key == " ")),
				"tiger selection keys must be ASCII punctuation; only the first may be space"
			)
			assert(not used[key], "tiger selection keys must be distinct")
			used[key] = true
		end
		assert(opts.matcher == nil or opts.matcher == "full_code", "tiger selection requires full_code matching")
	end
	assert(not opts.converter or not selection, "disable selection when using a code converter")
	local tables = require("flash-any.table")
	local data, ranks
	if opts.data or opts.lua then
		assert(not selection, "tiger ranked selection needs a file; set selection=false for Lua/data")
		data = opts.data and tables.normalize(opts.data) or tables.from_files(opts.lua, opts.tsv)
	else
		local file = opts.file or assert(vim.api.nvim_get_runtime_file("lua/flash-any/tables/tiger.tsv", false)[1])
		local input = opts.file and opts or { format = "tsv", columns = { "text", "code", "weight", "order" } }
		data, ranks = tables.from_file(file, vim.tbl_extend("force", input, { weights = not not selection }))
		if selection then
			-- Tiger codes contain letters; punctuation entries are complete codes without selectors.
			for code in pairs(assert(ranks)) do
				if not code:find("[a-zA-Z]") then
					ranks[code] = nil
				end
			end
		end
	end
	local selectors = selection and require("flash-any.build").selectors(data, assert(ranks), selection) or {}
	return {
		scope = "chinese",
		data = data,
		matcher = "full_code",
		prepared = true,
		selectors = selectors,
	}
end
